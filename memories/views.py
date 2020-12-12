from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User


def home(request):
    return render(request, 'memories/home.html')


# @login_required
def memories(request):
    return render(request, 'memories/memories.html')


def map(request):
    return render(request, 'memories/map.html')
