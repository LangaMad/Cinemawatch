from django.contrib import admin
from .models import User, Rank
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'avatar',

    ]

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        ]

