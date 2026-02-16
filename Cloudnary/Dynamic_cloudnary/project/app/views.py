from django.shortcuts import render
from .forms import ProfileForm
# Create your views here.

def landing(req):
    return render(req,'landing.html')


def upload_profile(req):
    if req.method == 'POST':
        form = ProfileForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        
    else:
        form = ProfileForm()


    return render(req, 'landing.html', {'form':form})


