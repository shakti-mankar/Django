from django.db import models

# Create your models here.

class Patient(models.Model):
        name = models.CharField(max_length=30)
        email= models.EmailField(max_length=30)
        address = models.CharField(max_length=30)
        city = models.CharField(max_length=30) 
        date = models.DateTimeField()
        time = models.TimeField()

        
    
