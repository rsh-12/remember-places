from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from django.views.generic import TemplateView

app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(template_name="user/profile.html"), name='profile'),
    path('password_change/',
         PasswordChangeView.as_view(template_name="registration/change_password.html"), name='password_change')
]
