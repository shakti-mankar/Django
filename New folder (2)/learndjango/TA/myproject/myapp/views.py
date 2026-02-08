from django.shortcuts import render

# Create your views here.
from .models import Student


def index(r):
    return render(r,'index.html')

def data(r):
    n=r.POST.get('name')
    e=r.POST.get('email')
    tel1=r.POST.get('tel1')
    tel2=r.POST.get('tel2')
    q = r.POST.getlist('qualifiaction')
    city=r.POST.get('city')
    g=r.POST.get('gender')
    pic=r.FILES.get('image')
    audio=r.FILES.get('audio')
    vid=r.FILES.get('video')
    d=r.FILES.get('Document')
    print(n,e,tel1,tel2,q,city,g,pic,audio,vid,d,sep=" ")
    Student.objects.create(name=n,email=e,contact=tel1,tel=tel2,quali=q,state=city,gender=g,img=pic,vid=vid,aud=audio,Document=d)



