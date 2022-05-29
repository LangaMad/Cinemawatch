from .models import Film, Celebrity
from random import shuffle
from random import random

def get_last_films(request):
    last_films = Film.objects.order_by("film_added")
    return {"last_films":last_films[:13]}

def get_announced_films(request):
    announced_films = Film.objects.filter(is_coming_soon=True)
    return {"announced_films":announced_films[:13]}

def get_rated_films(request):
    rated_films = Film.objects.order_by('-rating_critic')
    return {"rated_films":rated_films[:13]}

def get_celebrities(request):
    celebrities = sorted(Celebrity.objects.all().order_by("full_name"), key=lambda x: random())
    return {"celebrities":celebrities[:5]}

