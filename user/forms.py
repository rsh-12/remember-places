from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class BootstrapStylesMixin:
    field_names = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.field_names:
            for fieldname in self.field_names:
                self.fields[fieldname].widget.attrs = {'class': 'form-control col-md-4'}
        else:
            raise ValueError('The field_names must be set')


class UserPasswordResetForm(BootstrapStylesMixin, PasswordResetForm):
    field_names = ['email']


class UserSetPasswordForm(BootstrapStylesMixin, SetPasswordForm):
    field_names = ['new_password1', 'new_password2']


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
