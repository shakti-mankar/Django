from django.shortcuts import render

# Create your views here.


def login(req):
    return render(req,'login.html') 

def forget(req):
    return render(req,'forget.html')

  
def otp(req): 
    return render(req,'otp.html')

  
def newpassword(req):
    return render(req,'newpassword.html')

  