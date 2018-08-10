from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUp(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required Field. Please enter a valid email address')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')