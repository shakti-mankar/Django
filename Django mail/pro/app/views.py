from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def mail(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        contact = req.POST.get('contact')
        query = req.POST.get('query')

        print(name,email,contact,query,sep=',')


        send_mail(
            "Testing from django",
            f'email from {email} \n name:{name} \n contact:{contact} \n query:{query} ',
            email,
            ["mailshaktimankar@gmail.com",],
            fail_silently=False,
        )
        return HttpResponse('MAIL DONE')