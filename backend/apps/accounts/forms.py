

from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"name":"email",'id':'email-2'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "name":"password",
                'id':'password-2',
                "type":"password",
                "autocomplete":"off",
                "placeholder":"Пароль"
            }
            )
    )




class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"name":'password','id':'password-2'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"name": 'password','id':'repassword-2'}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',

        ]

    widgets = {
        "username": forms.TextInput(attrs={"name":'username','id':'username-2'}),
        "email": forms.EmailInput(attrs={"name":'email','id':'email-2'}),


    }






