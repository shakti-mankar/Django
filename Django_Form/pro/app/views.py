from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from .models import Student

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def formdata(req):
    print("hello data")
    print(req.method)
    print(req.POST)
    print(req.GET)
    print(req.FILES)
    n=req.POST.get('name')
    e=req.POST.get('email')
    c1=req.POST.get('Contact')
    c2=req.POST.get('Contact_2')
    q=req.POST.get('quali')
    s=req.POST.get('state')
    g=req.POST.get('gender')
    i=req.FILES.get('image')
    d=req.FILES.get('Doc')
    a=req.FILES.get('Audio')
    v=req.FILES.get('video')

    print(n,e,c1,c2,q,s,g,v,a,d,sep=',')

    Student.objects.create(Name=n,Email=e,Contact=c1,Contact_2=c2,quali=q,state=s,gender=g,
                           image=i,document=d,audio=a,video=v)






    
