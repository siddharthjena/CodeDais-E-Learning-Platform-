from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class signup(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','required': 'true'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','required': 'true'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control','required': 'true'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
        }