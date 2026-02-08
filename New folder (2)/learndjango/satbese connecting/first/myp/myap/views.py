from django.shortcuts import render

# Create your views here.
def  formdata(r):
    print(r.method)
    print(r.GET)
    print(r.POST)
    print(r.FILES)


def l(r):
    return render(r,'l.html')
    

    