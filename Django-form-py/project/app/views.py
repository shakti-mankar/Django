from django.shortcuts import render,redirect 
from .forms import StudentForm

# Create your views here.


def register(req):
    if req.method=='POST':
        # print("Hello")
        x = StudentForm(req.POST)
        if x.is_valid():
            print(x.cleaned_data)
            x.save()
            return redirect('login')

        # print(x)

    xyz = StudentForm()
    return render(req,'register.html', {'fm':xyz})


def login(req):
    return render(req,'login.html')

