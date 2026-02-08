from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def set(req):
    if req.method=='POST':
        n = req.POST.get('name')
        # e = req.POST.get('email')
        p = req.POST.get('pass')
        # print(n,e,p)
        req.session['name'] = n   
        req.session['email'] = req.POST.get('email')
        req.session['password'] = p
        return render(req,'landing.html')
    return render(req,'set.html')

def get(req):
    n = req.session['name']
    e = req.session.get('email')
    p = req.session.get('password')
    t = req.session.get('Neeraj','Guest')
    print(n,e,p,t)
    return render(req,'get.html',{'name':n,'email':e,'pass':p,'demo':t})

def delete(req):
        req.session.flush()
        return render(req,'delete.html')

