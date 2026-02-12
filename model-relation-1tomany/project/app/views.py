from django.shortcuts import render
from .models import *

# Create your views here.


def landing(req):
    return render(req,'landing.html')
    

def forward_access(req):
    #First method :- wihtout related name 
    data = Employee.objects.all()
    # print(data.query)

    for i in data:
        print(i.name,
              i.city,
              i.mobile,
              i.email,
              i.course,
              i.dep_data.d_disc)
        

    
        return render(req,'landing.html', 
                  {'data':data,
                  'forward_access':True})



def reverse_access(req):
    #without related name 
    data = Department.objects.prefetch_related('employee_set')
    print(data.query)

    for i in data:
        print(i.d_name,
              i.d_disc,
              i.employee_set.all())
    return render(req,'landing.html',{'data':data,'reverse_access':True})


