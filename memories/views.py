from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Place


def home(request):
    return render(request, 'memories/home.html')


# @login_required
def memories(request):
    user = User.objects.get(id=request.user.id)
    places = user.place_set.all()

    context = {'user': user, 'places': places}
    return render(request, 'memories/memories.html', context)


def map(request):
    return render(request, 'memories/map.html')
