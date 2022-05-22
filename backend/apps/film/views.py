
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Actor
# Create your views here.

class IndexPage(TemplateView):
    template_name = "index.html"

class CelebrityDetailView(DetailView):
    model = Actor
    template_name = 'celebrity_detail.html'
    context_object_name = "celebrity"