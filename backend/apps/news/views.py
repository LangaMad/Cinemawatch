from django.shortcuts import render
from .models import News
from django.views.generic import DetailView
# Create your views here.

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = "news"