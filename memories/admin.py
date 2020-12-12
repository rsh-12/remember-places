from django.contrib import admin

from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'latitude', 'longitude']
    list_filter = ['name', 'created_at']
