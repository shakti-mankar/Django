from django.contrib.auth.models import AbstractUser
from django.db import models


# ── Custom User ──────────────────────────────────────────────────────
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("user",  "User"),
        ("admin", "Admin"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")

    def __str__(self):
        return f"{self.username} ({self.role})"


# ── Product ──────────────────────────────────────────────────────────
class Product(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)  # INR
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ── Order ────────────────────────────────────────────────────────────
class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid",    "Paid"),
        ("failed",  "Failed"),
    )
    user              = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    product           = models.ForeignKey(Product,    on_delete=models.CASCADE, related_name="orders")
    amount            = models.DecimalField(max_digits=10, decimal_places=2)
    status            = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    razorpay_order_id = models.CharField(max_length=100, blank=True)
    created_at        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} — {self.user.username}"


# ── Payment ──────────────────────────────────────────────────────────
class Payment(models.Model):
    order      = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    payment_id = models.CharField(max_length=100)
    signature  = models.CharField(max_length=200)
    status     = models.CharField(max_length=20, default="pending")
    paid_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"