from django.shortcuts import render
from .models import *

# Create your views here.

def landing(req):
    return render(req,'landing.html')


# without related name
# def reverse_access(req):
#     data=Adhaar.objects.all()
#     for i in data:
#         print(i.aadhar_no,i.created_date,i.created_by,i.student.name,i.student.email,
#               i.student.contact,i.student.city) 

#     return render(req, 'landing.html', {
#         "reverse_access": True,
#         "data": data
#     })


 # with related_name
def reverse_access(req):
    data=Adhaar.objects.all()
    for i in data:   # related model name in lowercase (student) change into related_name(xyz)
        print(i.aadhar_no,i.create_date,i.create_by,i.xyz.name,i.xyz.email,
              i.xyz.contact,i.xyz.city) 
    return render(req,'landing.html',{'data':data})
     




# without related name
# def forward_access(req):
#     data = Student.objects.select_related('a_no').all()
#     print(data.query)

#     for i in data:
#         print(
#             i.name,
#             i.email,
#             i.contact,
#             i.city,
#             i.a_no.aadhar_no,
#             i.a_no.created_by
#         )

#     return render(req, 'landing.html', {
#         "forward_access": True,
#         "data": data
#     })


def forward_access(req):
    stu_data=Student.objects.select_related('aadhar_no')
    print(stu_data.query)
    print(list(stu_data))
    for i in stu_data:
        print(i.name,i.email,i.contact,i.city,i.aadhar_no.a_no,i.aadhar_no.create_date,i.aadhar_no.create_by)
    return render(req,'landing.html',{'stu_data':stu_data})