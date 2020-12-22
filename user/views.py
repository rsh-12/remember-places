from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# user registration
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from user.forms import UserUpdateModelForm


class UserRegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('memories:memories')

    def form_valid(self, form):
        result = super(UserRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateModelForm
    template_name = "user/profile.html"
    success_url = "/profile/update/{id}/"


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "registration/change_password.html"
    success_url = reverse_lazy('user:profile-update')
