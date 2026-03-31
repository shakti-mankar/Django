from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product, Order, Payment

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display  = ["username", "email", "role", "is_staff"]
    list_filter   = ["role"]
    fieldsets     = UserAdmin.fieldsets + (
        ("Role", {"fields": ("role",)}),
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ["name", "price", "is_active", "created_at"]
    list_filter   = ["is_active"]
    search_fields = ["name"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ["id", "user", "product", "amount", "status", "created_at"]
    list_filter   = ["status"]
    search_fields = ["user__username", "razorpay_order_id"]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display  = ["id", "order", "payment_id", "status", "paid_at"]
    search_fields = ["payment_id"]