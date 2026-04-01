from django.db import models

# Create your models here.


from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Job(models.Model):
    company = models.CharField(max_length=100)
    post = models.CharField(max_length=100)

    def __str__(self):
        return self.company


class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    age = models.IntegerField()
    resume = models.TextField()
    company = models.CharField(max_length=100)
    post = models.CharField(max_length=100)

    def __str__(self):
        return self.name