from dataclasses import field, fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *



class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = user
        fields = ['FullName', 'email', 'password1', 'password2']




# class pp(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields='__all__'

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = user
        fields = ['email', 'password']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=user
        fields=['Profilepic']
class reciteUpForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UploadRecite
        fields= '__all__'
class MESS(forms.ModelForm):
    class Meta:
        model= UserMessage
        fields= '__all__'