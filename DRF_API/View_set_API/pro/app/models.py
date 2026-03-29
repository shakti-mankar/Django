from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age =  models.IntegerField()
    contact = models.IntegerField()

    # def __str__(self):
    #     return self.name
    
class officers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    post = models.CharField(max_length=50)
    salary = models.IntegerField()
    



