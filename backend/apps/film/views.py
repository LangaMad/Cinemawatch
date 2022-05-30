
from django.shortcuts import render
from django.views.generic import TemplateView , DetailView
from .models import Film
from django.views.generic import TemplateView, DetailView
from django.views.generic import TemplateView, DetailView, ListView
from .models import Film, Celebrity
from itertools import chain
# Create your views here.

class IndexPage(TemplateView):
    template_name = "index.html"



class FilmDetailView(DetailView):
    model = Film
    template_name = 'film_single.html'
    context_object_name = "film"



class CelebrityListView(ListView):
    model = Celebrity
    paginate_by = 1
    template_name = 'celebrity_list.html'
    context_object_name = "celebrities"

class CelebrityDetailView(DetailView):
    model = Celebrity
    template_name = 'celebrity_detail.html'
    context_object_name = "celebrity"

class FilmListView(ListView):
    model = Film
    paginate_by = 2
    template_name = 'film_list.html'
    context_object_name = "films"