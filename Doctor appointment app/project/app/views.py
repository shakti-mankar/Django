
from django.shortcuts import render
from .models import Patient

def landing(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        date = request.POST.get('date')
        time = request.POST.get('time')

       
        Patient.objects.create(
            name=name,
            email=email,
            address=address,
            city=city,
            date=date,
            time=time
        )

        return render(request, 'success.html', {'success':Patient})  

    return render(request,'landing.html')


def success(req):
    return render(req,'success.html')




