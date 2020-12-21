from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'memories'

urlpatterns = [
    path('', TemplateView.as_view(template_name='memories/home.html'), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('memories/', views.PlaceListView.as_view(), name='memories'),
    path('memory/<int:pk>/', views.PlaceDetailView.as_view(), name='memory'),
    path('map/', views.PlaceCreateView.as_view(), name='map'),
    path('delete/<int:pk>/', views.PlaceDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.PlaceUpdateView.as_view(), name='update'),
]
