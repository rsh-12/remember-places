from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def home(request):
    return render(request, 'memories/home.html')


def login(request):
    return render(request, 'memories/login.html', {})


@login_required
def profile(request):
    return render(request, 'memories/profile.html')
