from .models import Place
from django import forms


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = [
            'name',
            'description'
        ]
