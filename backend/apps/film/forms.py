from django import forms
from .models import Comment

class FilmCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']