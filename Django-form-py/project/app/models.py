from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Age = models.IntegerField()
    City = models.CharField(max_length=30)

    def clean(self):
        errors = {}


        # Name validation
        if not self.Name.isalpha():
            errors['Name'] = "Name must contains only alphabets"

        elif len(self.Name) < 3 or len(self.Name) > 10:
            errors['Name'] = "Name must be between 3 and 10 characters"

        # age validation
        if self.Age <18 or self.Age > 60:
            errors['Age'] = "Age must be between 18 and 60"

        # Email validation
        if not self.Email.endswith("@gmail.com"):
            errors['Email'] = "Only Gmail email allowed"

        #City validation
        if not self.City.isalpha():
            errors['City'] = "City must contains only alphabets"

        if errors:
            raise ValidationError(errors)
        
    def save(self, *args, **kwrgs):
        self.full_clean()
        super().save(*args , **kwrgs)
        

    


