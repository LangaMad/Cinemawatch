from django import forms
from .models import Comment

class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
                "text": forms.Textarea(attrs={
                "placeholder": "Введите текст",
                "name":'message'
                    })
                }