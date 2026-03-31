from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Order, Payment

User = get_user_model()


# ── Auth Serializers ─────────────────────────────────────────────────
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model  = User
        fields = ["id", "username", "email", "password", "role"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ["id", "username", "email", "role"]


# ── Product Serializer ───────────────────────────────────────────────
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ["id", "name", "description", "price", "is_active"]


# ── Order Serializer ─────────────────────────────────────────────────
class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model  = Order
        fields = ["id", "product", "amount", "status", "razorpay_order_id", "created_at"]


# ── Payment Serializer ───────────────────────────────────────────────
class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model  = Payment
        fields = ["id", "order", "payment_id", "status", "paid_at"]


# ── Payment Verify Serializer ────────────────────────────────────────
class PaymentVerifySerializer(serializers.Serializer):
    razorpay_order_id   = serializers.CharField()
    razorpay_payment_id = serializers.CharField()
    razorpay_signature  = serializers.CharField()