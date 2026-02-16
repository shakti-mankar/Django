from django import forms
from .models import Profile


class ProfileForm(form.ModelForm):
    class Meta:
        model = Profile
        fiels = ['image','audio','video']
        