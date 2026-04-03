import razorpay
import hmac
import hashlib

from django.conf import settings
from django.contrib.auth import authenticate

from rest_framework.views     import APIView
from rest_framework.response  import Response
from rest_framework            import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.tokens import RefreshToken

from .models       import Product, Order, Payment
from .serializers  import (
    RegisterSerializer, UserSerializer,
    ProductSerializer,
    OrderSerializer, PaymentVerifySerializer, PaymentSerializer,
)

# Razorpay client (singleton)
rzp_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)


# ════════════════════════════════════════════════════════════════════
#  AUTH VIEWS
# ════════════════════════════════════════════════════════════════════

class RegisterView(APIView):
    """POST /api/register/ — public"""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user    = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user":    UserSerializer(user).data,
                "refresh": str(refresh),
                "access":  str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """POST /api/login/ — public"""
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user     = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "user":    UserSerializer(user).data,
                "refresh": str(refresh),
                "access":  str(refresh.access_token),
            })
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class ProfileView(APIView):
    """GET /api/profile/ — authenticated"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


# ════════════════════════════════════════════════════════════════════
#  PRODUCT VIEWS
# ════════════════════════════════════════════════════════════════════

class ProductListView(APIView):
    """GET /api/products/ — authenticated"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.filter(is_active=True)
        return Response(ProductSerializer(products, many=True).data)


class ProductCreateView(APIView):
    """POST /api/products/create/ — admin only"""
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    """GET /api/products/<pk>/ — authenticated"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk, is_active=True)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(ProductSerializer(product).data)


# ════════════════════════════════════════════════════════════════════
#  PAYMENT VIEWS
# ════════════════════════════════════════════════════════════════════

class CreateOrderView(APIView):
    """POST /api/payments/create-order/ — authenticated"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")

        try:
            product = Product.objects.get(id=product_id, is_active=True)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        amount_paise = int(product.price * 100)  # Razorpay works in paise

        # Create order in Razorpay
        razorpay_order = rzp_client.order.create({
            "amount":          amount_paise,
            "currency":        "INR",
            "payment_capture": 1,
        })

        # Save order in DB
        order = Order.objects.create(
            user=request.user,
            product=product,
            amount=product.price,
            razorpay_order_id=razorpay_order["id"],
        )

        return Response({
            "order_id":     razorpay_order["id"],
            "amount":       amount_paise,
            "currency":     "INR",
            "key":          settings.RAZORPAY_KEY_ID,
            "db_order_id":  order.id,
            "product_name": product.name,
        }, status=status.HTTP_201_CREATED)


class VerifyPaymentView(APIView):
    """POST /api/payments/verify/ — authenticated"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PaymentVerifySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        # ── Signature verification ───────────────────────────────────
        body         = f"{data['razorpay_order_id']}|{data['razorpay_payment_id']}"
        expected_sig = hmac.new(
            settings.RAZORPAY_KEY_SECRET.encode(),
            body.encode(),
            hashlib.sha256,
        ).hexdigest()

        if expected_sig != data["razorpay_signature"]:
            return Response(
                {"error": "Invalid payment signature"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # ── Update Order ─────────────────────────────────────────────
        try:
            order = Order.objects.get(razorpay_order_id=data["razorpay_order_id"])
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        order.status = "paid"
        order.save()

        # ── Create Payment record ────────────────────────────────────
        Payment.objects.create(
            order=order,
            payment_id=data["razorpay_payment_id"],
            signature=data["razorpay_signature"],
            status="success",
        )

        return Response({"message": "Payment verified successfully!"})


class PaymentHistoryView(APIView):
    """GET /api/payments/history/ — authenticated user's own payments"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.filter(
            order__user=request.user
        ).select_related("order", "order__product").order_by("-paid_at")
        return Response(PaymentSerializer(payments, many=True).data)


class AllPaymentsView(APIView):
    """GET /api/payments/all/ — admin only"""
    permission_classes = [IsAdminUser]

    def get(self, request):
        payments = Payment.objects.select_related(
            "order", "order__user", "order__product"
        ).order_by("-paid_at")
        return Response(PaymentSerializer(payments, many=True).data)