from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.IntegerField()
    Contact_2 = models.IntegerField()
    quali = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',null=True)
    document = models.FileField(upload_to='doc/',null=True)
    audio = models.FileField(upload_to='audio/',null=True)
    video =  models.FileField(upload_to='video/',null=True)

    def __str__(self):
        return self.Name + " " + self.Email + " " + str(self.Contact)

