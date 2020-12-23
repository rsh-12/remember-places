from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView
from django.urls import path

from user.views import *

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='profile-update'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),

    # path('password_reset/', PasswordResetView.as_view(
    #     template_name='user/reset_password.html'), name='password_reset'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),

    # path('password_reset/done/', PasswordResetDoneView.as_view(
    #     template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),

    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #     template_name='user/password_reset_confirm.html', success_url='/password_reset/done/'),
    #      name='password_reset_confirm'),
    path('reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
