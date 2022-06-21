

from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm



class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class":"form-input","placeholder":"Никнейм"})
    )

    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-input","placeholder":"Почта"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-input",
                "placeholder":"Пароль"
            }
            )
    )




class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Пароль"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Повторите пароль"}))

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Никнейм"})
    )

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-input", "placeholder": "Почта"}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]







class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            "avatar",

        ]


class PasswordChangingForm(PasswordChangeForm):



    class Meta:
        model = User
        fields = [
            "old_password",
            'new_password',
            'new_password2'
        ]









