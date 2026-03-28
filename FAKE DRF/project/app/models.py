from django.db import models

# Create your models here.

class Empserialiazers(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.IntegerField()
    age = models.IntegerField()


    

