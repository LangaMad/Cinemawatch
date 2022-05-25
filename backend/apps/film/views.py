
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Actor, Director
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