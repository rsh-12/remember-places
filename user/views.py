from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# user registration
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserRegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('memories:memories')

    def form_valid(self, form):
        result = super(UserRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result
