from django.db import models


# Create your models here.

class Department(models.Model):
    d_name = models.CharField(max_length=30)
    d_disc = models.TextField()

    def __str__(self):
        return self.d_name
    

class Employee(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    mobile = models.IntegerField(max_length=30)
    email = models.EmailField(max_length=30)
    course = models.CharField(max_length=30)
    dep_data = models.ForeignKey(Department,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


