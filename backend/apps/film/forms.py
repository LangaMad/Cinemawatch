from django import forms
from .models import Comment, Rating, RatingStar

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


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None

    )
    class Meta:
        model = Rating
        fields = ['star',]