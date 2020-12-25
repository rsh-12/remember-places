from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from user.forms import *


# user registration
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


# update user profile (firstname, lastname, email)
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateModelForm
    template_name = "user/profile.html"

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request, 'Profile updated successfully!')
            form.save()
            return render(self.request, 'user/profile.html', {'form': form})
        messages.warning(self.request, 'Something went wrong! Please try again!')
        return render(self.request, 'user/profile.html', {'form': form})


# update user password
class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "user/change_password.html"

    def get_success_url(self):
        messages.success(self.request, 'Password updated successfully!')
        return reverse('user:profile-update', kwargs={'pk': self.request.user.id})


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'user/reset_password.html'
    success_url = reverse_lazy('user:password_reset_done')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(UserPasswordResetView, self).get(request, *args, **kwargs)


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user/password_reset_done.html'
    success_url = '/profile/reset/<uidb64>/<token>/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(UserPasswordResetDoneView, self).get(request, *args, **kwargs)


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    template_name = 'user/password_reset_confirm.html'
    success_url = reverse_lazy('user:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'user/password_reset_complete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(UserPasswordResetCompleteView, self).get(request, *args, **kwargs)
