
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Actor, Director, Film
from itertools import chain
# Create your views here.

class IndexPage(TemplateView):
    template_name = "index.html"

class CelebrityListView(ListView):
    model = Actor
    template_name = 'celebrity_list.html'


class CelebrityDetailView(DetailView):
    model = Actor
    template_name = 'celebrity_detail.html'
    context_object_name = "celebrity"

class FilmListView(ListView):
    model = Film
    paginate_by = 2
    template_name = 'film_list.html'
    context_object_name = "films"