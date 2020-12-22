from django import forms
from django.contrib.auth.models import User


class UserUpdateModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form form-control col-md-6',
                                                 'placeholder': 'enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form form-control col-md-6',
                                                'placeholder': 'enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form form-control col-md-6',
                                             'placeholder': 'enter email'})
        }
