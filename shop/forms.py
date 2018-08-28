from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUp(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Required Field. Please enter a valid email address')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class MyForm(forms.Form):
    sizes_c = (
        "Small",
        "Medium",
        "Large",
    )
    my_choice_field = forms.ChoiceField(choices=sizes_c)