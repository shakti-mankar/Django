from django.contrib import admin
from django.urls    import path
from rest_framework_simplejwt.views import TokenRefreshView

from app.views import (
    # Auth
    RegisterView, LoginView, ProfileView,
    # Products
    ProductListView, ProductCreateView, ProductDetailView,
    # Payments
    CreateOrderView, VerifyPaymentView,
    PaymentHistoryView, AllPaymentsView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # ── Auth ──────────────────────────────────────────────────────
    path("api/register/",     RegisterView.as_view(),    name="register"),
    path("api/login/",        LoginView.as_view(),       name="login"),
    path("api/profile/",      ProfileView.as_view(),     name="profile"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ── Products ──────────────────────────────────────────────────
    path("api/products/",          ProductListView.as_view(),   name="product-list"),
    path("api/products/create/",   ProductCreateView.as_view(), name="product-create"),
    path("api/products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),

    # ── Payments ──────────────────────────────────────────────────
    path("api/payments/create-order/", CreateOrderView.as_view(),    name="create-order"),
    path("api/payments/verify/",       VerifyPaymentView.as_view(),  name="verify-payment"),
    path("api/payments/history/",      PaymentHistoryView.as_view(), name="payment-history"),
    path("api/payments/all/",          AllPaymentsView.as_view(),    name="all-payments"),
]