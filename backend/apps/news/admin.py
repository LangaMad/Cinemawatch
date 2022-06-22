from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from django import forms
# Register your models here.

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = News
        fields = '__all__'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
    'title',
    'text',
    'poster',
    'image',
    'created',

    ]
    form = NewsAdminForm

@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = [
    'title',
    'link',
    'long_time',
    'added',
    ]

@admin.register(NewsTag)
class NewsTagAdmin(admin.ModelAdmin):
    list_display = [
    'name',
    ]