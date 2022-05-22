from .models import Film, Actor
from random import randint

def get_last_films(request):
    last_films = Film.objects.order_by("film_added")
    return {"last_films":last_films[:13]}

def get_announced_films(request):
    announced_films = Film.objects.filter(is_coming_soon=True)
    return {"announced_films":announced_films[:13]}

def get_rated_films(request):
    rated_films = Film.objects.order_by('-rating_critic')
    return {"rated_films":rated_films[:13]}

def get_actors(request):
    actors = Actor.objects.all()
    return {"actors":actors[:5]}
