from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Place
from .forms import PlaceForm


def home(request):
    return render(request, 'memories/home.html')


# @login_required
def memories(request):
    user = User.objects.get(id=request.user.id)
    places = user.place_set.all()

    context = {'user': user, 'places': places}
    return render(request, 'memories/memories.html', context)


def memory(request, pk):
    place = Place.objects.get(id=pk)
    context = {'place': place}
    return render(request, 'memories/memory.html', context)


def create_place(request):
    form = PlaceForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'memories/map.html', context)
