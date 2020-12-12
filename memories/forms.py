from .models import Place
from django import forms


class RawPlaceForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()
