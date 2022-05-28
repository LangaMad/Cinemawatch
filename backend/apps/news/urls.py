from django.urls import path
from .views import *
urlpatterns = [
        path('detail/<int:pk>/',NewsDetailView.as_view(), name='news_detail')
    ]