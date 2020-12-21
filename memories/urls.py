from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from django.views.generic import TemplateView

from .views import UserRegistrationView

app_name = 'memories'

urlpatterns = [
    path('', TemplateView.as_view(template_name='memories/home.html'), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('memories/', views.PlaceListView.as_view(), name='memories'),
    path('memory/<int:pk>/', views.PlaceDetailView.as_view(), name='memory'),
    path('map/', views.PlaceCreateView.as_view(), name='map'),
    path('delete/<int:pk>/', views.PlaceDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.PlaceUpdateView.as_view(), name='update'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/registration/', UserRegistrationView.as_view(), name='registration'),
    path('accounts/password_change/',
         PasswordChangeView.as_view(template_name="registration/password_change_form.html"), name='password_change'),
    path('profile/', TemplateView.as_view(template_name="memories/profile.html")),
]
