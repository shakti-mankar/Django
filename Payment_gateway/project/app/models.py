from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    brand = models.CharField(max_length=20)
    description = models.CharField(max_length=60)

