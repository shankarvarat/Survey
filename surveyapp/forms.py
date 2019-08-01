from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *




class questionform(forms.ModelForm):
    class Meta:
        model = question
        fields = '__all__'