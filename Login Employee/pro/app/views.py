from django.shortcuts import render , redirect
from django.contrib import messages



# Create your views here.

def index(req):
    messages.info(req,"Wellcome to my page")
    messages.debug(req,"This is debug alert")
    messages.error(req," Something went wrong ")
    messages.success(req," Successfully completed ")
    messages.warning(req," Error 404 ")
    return redirect('home')


def home(req):
    return render(req,'home.html')


