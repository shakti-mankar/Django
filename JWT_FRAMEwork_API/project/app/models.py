from django.db import models

# Create your models here.

role = (('admin', 'admin'), ('staff' , 'staff') , ('user' , 'user'))

class Employee(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_email = models.EmailField()
    emp_department = models.CharField()
    emp_role = models.CharField(max_length=20 , choices=role)

    def __str__(self):
        return self.emp_name
    