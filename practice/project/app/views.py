from django.shortcuts import render , redirect
from django .http import HttpResponse , JsonResponse

# Create your views here.

def text(req):
    return HttpResponse("this is shaktiman")

def html(req):
    return HttpResponse(" <h1>this is shaktiman </h1>")


def redirect(req):
    return redirect('https://www.google.com')
