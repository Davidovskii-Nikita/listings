from django.conf import settings
from django.contrib import auth
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, CreateView

from .forms import LoginForm, RegForm


# class LoginView(LoginView):
#     form_class = LoginForm
#     template_name = 'registation/login.html'
#     success_url = reverse_lazy('login')
#
# class RegView(CreateView):
#     form_class = RegForm
#     template_name = 'registation/login.html'
#     success_url = reverse_lazy('index')

class AuthView(TemplateView):
    template_name = 'registation/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg_form'] = RegForm
        context['log_form'] = LoginForm
        return context

    @method_decorator(csrf_protect)
    def post(self, request = HttpRequest, *args, **kwargs):
        if request.method == 'POST':
            if 'log' in request.POST:
                user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        return HttpResponseRedirect('account/profile')
                    return HttpResponseRedirect('login/')

            if 'reg' in request.POST:
                reg_form = RegForm(request.POST)
                username = request.POST['username']
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                email = request.POST['email']
                context = {
                    'username': username,
                    'password1': password1,
                    'password2': password2,
                    'email': email}
                if reg_form.is_valid():
                    # Create a new user object but avoid saving it yet
                    new_user = reg_form.save(commit=False)
                    # Set the chosen password
                    new_user.set_password(reg_form.cleaned_data['password1'])
                    new_user.email = email
                    # Save the User object
                    new_user.save()
                    return render(request, 'listing/listing.html', {'new_user': new_user})

        return self.get(request=request)