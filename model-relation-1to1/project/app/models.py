from django.db import models

# Create your models here.

class Adhaar(models.Model):
    aadhar_no = models.IntegerField()
    created_date = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.aadhar_no)


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.IntegerField()
    city = models.CharField()
    a_no = models.OneToOneField(Adhaar,on_delete=models.CASCADE)

