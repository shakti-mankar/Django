from django.db import models

# Create your models here.

class emp(models.Model):
    fname=models.CharField(max_length=50,null=True,blank=True)
    lname=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    img=models.ImageField()
    adhaar=models.ImageField()
    code=models.CharField(max_length=50,null=True,blank=True)
    mobile=models.CharField(max_length=50,null=True,blank=True)
    dob=models.CharField(max_length=50,null=True,blank=True)
    gender=models.CharField(max_length=50,null=True,blank=True)
    edu=models.CharField(max_length=50,null=True,blank=True)
    dept=models.CharField(max_length=50,null=True,blank=True)



class dep(models.Model):
    dept_name=models.CharField(max_length=50,null=True,blank=True)
    dept_code=models.CharField(max_length=50,null=True,blank=True,unique=True)
    dept_head=models.CharField(max_length=50,null=True,blank=True)
    dept_budget=models.CharField(max_length=50,null=True,blank=True)
    dept_desc=models.CharField(max_length=50,null=True,blank=True)
    dept_emp=models.CharField(max_length=50,null=True,blank=True)




class query(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Query=models.TextField()
    department=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default='pending')
    admin_rep=models.CharField(blank=True)


