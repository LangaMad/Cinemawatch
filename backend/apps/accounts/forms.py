

from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class":"form-input","placeholder":"Username"})
    )

    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-input","placeholder":"Email"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-input",
                "placeholder":"Password"
            }
            )
    )




class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Пароль"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Повторите пароль"}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

    widgets = {
        "username": forms.TextInput(
            attrs={
                "class":"form-input",
                "placeholder":"Usrname"}
        ),
        "email": forms.EmailInput(attrs={"class":"form-input", "placeholder":"Email"}),


    }






