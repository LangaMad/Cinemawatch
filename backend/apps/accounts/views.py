
from django.shortcuts import render,redirect
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView)
from django.contrib.auth import login,authenticate,logout
from  django.http import HttpResponse

from django.urls import reverse_lazy



from .forms import LoginForm,UserRegisterForm
# Create your views here.
class LoginView(FormView):

    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт неактивен')
        return HttpResponse('Такого юзера не существует')

class UserRegisterView(CreateView):

    form_class = UserRegisterForm



def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')




