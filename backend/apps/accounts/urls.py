from django.urls import path

from .views import *

urlpatterns = [
        path('sign_up/', UserRegisterView.as_view(), name = 'sign_up'),
        path('sign_in/', LoginView.as_view(), name = 'sign_in'),
        path('logout/', UserLogout, name = 'logout')
]