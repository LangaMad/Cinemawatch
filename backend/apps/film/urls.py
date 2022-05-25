from django.urls import path

from .views import *

urlpatterns = [
        path('', IndexPage.as_view(), name='index'),
        path('celebrity/detail/<int:pk>/', CelebrityDetailView.as_view(), name='celebrity_detail'),
        path('list/', CelebrityListView.as_view(), name='celebrity_list')
]