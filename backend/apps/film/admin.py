from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = [
    'id',
    'full_name',
    'birthday',
    'country',
    'is_alive',
    'biography',
    'image',
    ]
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = [
    'id',
    'full_name',
    'birthday',
    'country',
    'is_alive',
    'biography',
    'image',
    ]
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
    'name',
    'slug',
    'id',
    ]
    prepopulated_fields = {'slug': ('name',)}


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
    'relise_date',
    'country',
    'long_time',
    'film_added',

    ]

