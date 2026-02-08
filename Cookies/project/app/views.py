from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    return render(request, 'landing.html')


# ---------------- SET COOKIE ----------------
def set(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('pass')

        response = render(request, 'landing.html')
        response.set_cookie('name', n, max_age=60*60)
        response.set_cookie('email', e)
        response.set_cookie('password', p)

        return response

    return render(request, 'set.html')


# ---------------- GET COOKIE ----------------
def get(request):
    print(request.COOKIES)

    c = request.COOKIES.get('csrftoken')
    n = request.COOKIES.get('name')
    e = request.COOKIES.get('email')
    p = request.COOKIES.get('password')
    t = request.COOKIES.get('Shakti', 'Guest')

    print(c, n, e, p, t)
    return render(request, 'get.html',{'name':n,'email':e,'pass':p,'demo':t})
    


# ---------------- DELETE COOKIE ----------------
def delete(request):
    response = render(request, 'delete.html')

    if 'name' in request.COOKIES:
        response.delete_cookie('name')

    if 'email' in request.COOKIES:
        response.delete_cookie('email')

    if 'password' in request.COOKIES:
        response.delete_cookie('password')

    return response
