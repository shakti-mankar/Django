from django.shortcuts import render,redirect 
from .forms import StudentForm

# Create your views here.


def register(req):
    if req.method=='POST':
        # print("Hello")
        x = StudentForm(req.POST)
        # print(x.is_valid)
        # print(x.errors)
        print(dict(x.errors))
        if x.is_valid():
            print(x.cleaned_data)
            x.save()
            return redirect('login')

        # print(x)

    else:
        x = StudentForm()
    return render(req,'register.html', {'fm':x})


def login(req):
    return render(req,'register.html')

