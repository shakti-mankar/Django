from django import forms
from .models import Student


# class StudentForm(forms.Form):
#     Name = forms.CharField()
#     Email = forms.EmailField()
#     age = forms.IntegerField()
#     City  = forms.CharField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'