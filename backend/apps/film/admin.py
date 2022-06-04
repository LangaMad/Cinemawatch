from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from django import forms
# Register your models here.



class CelebrityAdminForm(forms.ModelForm):
    biography = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Celebrity
        fields = '__all__'

class FilmAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Film
        fields = '__all__'

@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = [
    'id',
    'full_name',
    'birthday',
    'country',
    'is_alive',
    'short_biography',
    'biography',
    'image',
    ]

    form = CelebrityAdminForm

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
    'name',
    'slug',
    'id',
    ]
    prepopulated_fields = {'slug': ('name',)}



@admin.register(FilmsPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'film',
        'photo',
    ]

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = [
    'name',
    'description',
    'image',
    'film',
    'age_control',
    'is_coming_soon',
    'rating_critic',
    'rating_viewer',
    'date_relise',
    'country',
    'long_time',
    'film_added',
    ]
    filter_horizontal = [
        'actors',
        'directors',
        'genres'
    ]

    form = FilmAdminForm
