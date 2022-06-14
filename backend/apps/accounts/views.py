from django.shortcuts import render,redirect
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView,
    UpdateView)
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse,Http404,HttpResponseForbidden
from .models import User
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from .forms import UserUpdateForm


from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView




from .forms import LoginForm,UserRegisterForm
# Create your views here.
class LoginView(FormView):
    template_name = 'sign_in.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username  = data['username']
        email = data['email']
        password = data['password']
        user = authenticate(username=username,email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт неактивен')
        return HttpResponse('Такого юзера не существует')

class UserRegisterView(CreateView):
    template_name = 'sign_up.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')



def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')




class UserUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,PasswordChangeView):
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('index')
    queryset = User.objects.all()


    def test_func(self):
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False


# class PasswordsChangeView(PasswordChangeView):
#     form_class = PasswordChangingForm
#     template_name = 'user_update.html'
#     success_url = reverse_lazy('index')




































# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'user_update.html', {
#         'form': form
#     })

# from django.contrib.auth.decorators import login_required
#
# @login_required
# def update_user_profile(request, pk):
#     if request.user.pk != pk:
#         return HttpResponseForbidden()
#     if request.method == "POST":
#         form = AvatarUpdateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index',pk=pk)
#     else:
#         try:
#             user=User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#         form = AvatarUpdateForm(instance=user)
#     context = {
#         "form":form
#     }
#     return render(request, 'user_profile.html', context)




