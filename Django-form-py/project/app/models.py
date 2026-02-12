from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Age = models.IntegerField()
    City = models.CharField(max_length=30)

    


