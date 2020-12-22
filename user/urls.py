from django.contrib.auth.views import PasswordChangeView, LoginView, PasswordChangeDoneView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from user.views import *

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='profile-update'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
]
