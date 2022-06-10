from django.urls import path

from .views import *

urlpatterns = [
        path('', IndexPage.as_view(), name='index'),
        path('film/detail/<int:pk>/', get_film_detail, name='film_single'),
        path('celebrity/detail/<int:pk>/', CelebrityDetailView.as_view(), name='celebrity_detail'),
        path('celebrity/list/', CelebrityListView.as_view(), name='celebrity_list'),
        path('film/list/', FilmListView.as_view(), name='film_list'),
        path("add-rating/", AddStarRating.as_view(), name='add_rating'),
]