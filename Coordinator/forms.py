from django import forms

from users.models import user
from .models import *
from django.contrib.auth.models import User
class addCourse(forms.ModelForm):
    class Meta:
        model= course
        fields = '__all__'

class u_form(forms.ModelForm):
    class Meta:
        model = user 
        fields= ['email', 'password']

class addStud(forms.ModelForm):
    class Meta:
        model = user
        fields = ['FullName','course','Roll']
class valStud(forms.ModelForm):
    class Meta:
        model = user
        fields = ['Roll','Academy','course']

