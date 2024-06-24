from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class signup(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')