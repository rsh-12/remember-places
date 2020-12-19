from django import forms

from memories.models import Place


class PlaceModelForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ('user',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form form-control col-md-6',
                                           'placeholder': 'give a name to this place'}),
            'description': forms.Textarea(attrs={'class': 'form form-control col-md-6',
                                                 'rows': 5,
                                                 'placeholder': 'tell about your impressions'}),
            'latitude': forms.TextInput(),
            'longitude': forms.TextInput()
        }


class PlaceUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form form-control col-md-6',
                                           'placeholder': 'give a name to this place'}),
            'description': forms.Textarea(attrs={'class': 'form form-control col-md-6',
                                                 'rows': 5,
                                                 'placeholder': 'tell about your impressions'})}
