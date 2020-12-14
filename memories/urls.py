from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views
from django.views.generic import TemplateView

app_name = 'memories'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', TemplateView.as_view(template_name='memories/home.html'), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('memories/', views.memories, name='memories'),
    path('memory/<int:pk>/', views.memory, name='memory'),
    path('map/', views.create_place, name='map'),
]
