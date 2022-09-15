from dataclasses import fields
from django import forms

from users.models import user
from .models import *


class Add_Academy(forms.ModelForm):
    class Meta:
        model = Academy
        fields = '__all__'
class valStud(forms.ModelForm):
    class Meta:
        model = user
        fields = ['Roll']
class AddCoordinator(forms.ModelForm):
    class Meta:
        model = user
        fields = ['FullName','Roll']
class ICT(forms.ModelForm):
    class Meta:
        model= ICTDescription
        fields= '__all__'