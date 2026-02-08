from django.db import models

# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Query = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    
