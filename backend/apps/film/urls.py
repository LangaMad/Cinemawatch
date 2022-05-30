from django.urls import path

from .views import *

urlpatterns = [
        path('', IndexPage.as_view(), name='index'),
        path('film/detail/<int:pk>/',FilmDetailView.as_view(), name='film_single'),
        path('celebrity/detail/<int:pk>/', CelebrityDetailView.as_view(), name='celebrity_detail'),
        path('celebrity/list/', CelebrityListView.as_view(), name='celebrity_list'),
        path('film/list/', FilmListView.as_view(), name='film_list'),
]