from .models import Place
from django import forms


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = [
            'name',
            'description',
            'latitude',
            'longitude',
            'users'
        ]


class RawPlaceForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()
    # users = Place.users.add()
