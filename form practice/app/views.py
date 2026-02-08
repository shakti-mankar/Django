from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def formdata(req):
    print("Hello world")
    print(req.method)
    print(req.POST)
    print(req.GET)
    print(req.files)

    