from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
    'title',
    'text',
    'image',
    'created',

    ]

@admin.register(Trailer)
class TailerAdmin(admin.ModelAdmin):
    list_display = [
    'title',
    'link',

    ]
