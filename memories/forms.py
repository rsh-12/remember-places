from django import forms


# form to add place
class RawPlaceForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form form-control col-md-6',
        'placeholder': 'give a name to this place'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form form-control col-md-6',
        'placeholder': 'tell about your impressions'}))

    latitude = forms.DecimalField(widget=forms.TextInput())
    longitude = forms.DecimalField(widget=forms.TextInput())
