from django.urls import path

from .views import *

urlpatterns = [
        path('', BasePage.as_view(), name='base'),


]