from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'memories'

urlpatterns = [
    path('', TemplateView.as_view(template_name='memories/home.html'), name='home'),
    path('memories/', views.PlaceListView.as_view(), name='memories'),
    path('memory/<int:pk>/', views.PlaceDetailView.as_view(), name='memory'),
    path('map/', views.PlaceCreateView.as_view(), name='map'),
    path('delete/<int:pk>/', views.PlaceDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.PlaceUpdateView.as_view(), name='update'),
    # path('search/', views.SearchPlaceListView.as_view(), name='search_places'),
]
