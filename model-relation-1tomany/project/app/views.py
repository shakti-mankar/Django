from django.shortcuts import render
from .models import *

# Create your views here.


def landing(req):
    return render(req,'landing.html')
    

def forward_access(req):
    #First method
    data = Employee.objects.all()
    # print(data.query)

    for i in data:
        print(i.name,
              i.city,
              i.mobile,
              i.email,
              course,
              i.dep_data.d_disc)
        

    return render(req,'landing.html', 
                  {'data':data},
                  "forward_access")



def reverse_access(req):
    return render(req,'landing.html')
