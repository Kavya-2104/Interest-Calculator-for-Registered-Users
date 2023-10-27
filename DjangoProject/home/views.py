from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView


def success(request):
  return HttpResponse('<h1> REGISTER SUCCESSFULL</h1>')

class SignupView(CreateView):
  form_class = UserCreationForm
  template_name = 'home/register.html'
  success_url = '/mbp/profs'

  def get(self,request, *args, **kwargs):
    if self.request.user.is_authenticated:
         return redirect('profile.list')
    return super().get(request,*args,**kwargs)

class LogoutInterfaceView(LogoutView):
  template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
  template_name = 'home/login.html'

class SuccessView(TemplateView):
  template_name = 'home/success.html'

class HomeView(TemplateView):
  template_name = 'home/welcome.html'

class AuthView(LoginRequiredMixin,TemplateView):
  template_name = 'home/authorized.html'
  login_url = '/admin'