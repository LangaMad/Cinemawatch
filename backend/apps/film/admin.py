from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = [
    'name',
    'age',
    'is_alive',
    'biography',
    'image',
    'id',
    ]
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = [
    'name',
    'age',
    'is_alive',
    'biography',
    'image',
    'id',
    ]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
    'name',
    'slug',
    'id',
    ]
    prepopulated_fields = {'slug': ('name',)}




