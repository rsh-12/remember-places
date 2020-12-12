from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Place
from .forms import PlaceForm, RawPlaceForm


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
