from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Passwords

class SignUpForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "type":"text",
        "placeholder":"username" ,
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        "type":"email",
        "placeholder":"email", 
    }))
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={
        "placeholder":"password"
    }))
    password2=forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={
        "placeholder":"password confirmation",
        "label":"password confirmation"
    }))
    
    class Meta:
        model=User
        fields=("username","email","password1","password2")

class PasswordForm(forms.ModelForm):
    password=forms.CharField(widget=forms.TextInput(attrs={
        "id":"pass"
    }))
    username=forms.CharField(label="username/email")
    class Meta:
        model=Passwords
        fields=("account","username","password")