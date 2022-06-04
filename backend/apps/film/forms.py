from django import forms
from .models import Comment

class FilmCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            "text": forms.TextInput(attrs={
            "type":"text",
            "name":'username',
            "id":"username-2",
            "placeholder":"Введите текст",
            })
        }