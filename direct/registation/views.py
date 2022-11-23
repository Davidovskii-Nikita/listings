from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import LoginForm, RegForm


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'registation/login.html'
    success_url = reverse_lazy('login')

class RegView(CreateView):
    context_object_name = 'form2'
    form_class = RegForm
    template_name = 'registation/login.html'
    success_url = reverse_lazy('index')