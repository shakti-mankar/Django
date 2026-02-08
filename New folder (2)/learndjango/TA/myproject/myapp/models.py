from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact = models.CharField(max_length=15,null=True)
    # tel=models.IntegerField(null=True,blank=True)
    tel=models.BigIntegerField(null=True,blank=True)
    quali=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    # img=models.ImageField(null=True,upload_to='img')
    img=models.ImageField(null=True,upload_to='img/')
    vid=models.FileField(null=True,upload_to='vid/')
    aud=models.FileField(null=True)
    Document=models.FileField()
    l=models.FileField(null=True)

    
    # def __str__(self):
    #      return self.name +" "+self.email+" "+self.contact

