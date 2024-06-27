from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    domain = forms.CharField(max_length=25)
    name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('name', 'email', 'domain', 'username', 'password1', 'password2')



