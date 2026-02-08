from django.shortcuts import render , redirect

# Create your views here.
from django.urls import reverse

from urllib.parse import urlencode



def my_redirect1(req):
    url = reverse('my_redirect2')
    data = urlencode({'name':'Neeraj' , 'age':37})

    return redirect (f'{url} ? {data}')



def my_redirect2(req):
    print("hello")
    print(req.get)
