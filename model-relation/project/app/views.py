from django.shortcuts import render
from .models import *

# Create your views here.

def landing(req):
    return render(req,'landing.html')


def reverse_access(req):
    data = Adhaar.objects.all()

    for i in data:
        print(
            i.aadhar_no,
            i.created_date,
            i.created_by
        )

    return render(req, 'landing.html', {
        "reverse_access": True,
        "data": data
    })

def forward_access(req):
    data = Student.objects.select_related('a_no').all()
    print(data.query)

    for i in data:
        print(
            i.name,
            i.email,
            i.contact,
            i.city,
            i.a_no.aadhar_no,
            i.a_no.created_by
        )

    return render(req, 'landing.html', {
        "forward_access": True,
        "data": data
    })
