from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.core.paginator import Paginator

from .forms import RawPlaceForm
from .models import Place

import os


def home(request):
    return render(request, 'memories/home.html')


@login_required
def memories(request):
    user = User.objects.get(id=request.user.id)
    places = user.place_set.all().order_by('-created_at')
    paginator = Paginator(places, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'user': user, 'places': places, 'page_obj': page_obj}
    return render(request, 'memories/memories.html', context)


@login_required
def memory(request, pk):
    place = Place.objects.get(id=pk)
    context = {'place': place}
    return render(request, 'memories/memory.html', context)


@login_required
def create_place(request):
    my_form = RawPlaceForm()
    if request.method == 'POST':
        my_form = RawPlaceForm(request.POST)
        if my_form.is_valid():
            user = User.objects.get(id=request.user.id)
            place = Place.objects.create(**my_form.cleaned_data)
            place.users.add(user)
            return redirect('memories:memories')
        else:
            print(my_form.errors)
    context = {'form': my_form}
    return render(request, 'memories/map.html', context)
