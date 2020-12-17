import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from .forms import RawPlaceForm
from .models import Place

logger = logging.getLogger(__name__)


# get all memories
@login_required
def memories(request):
    user = User.objects.get(id=request.user.id)
    logger.info("get current user")

    places = user.place_set.all().order_by('-created_at')
    logger.info("get all the user places")

    paginator = Paginator(places, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'user': user, 'places': places, 'page_obj': page_obj}
    return render(request, 'memories/memories.html', context)


# get memory by id
@login_required
def memory(request, pk):
    place = Place.objects.get(id=pk)
    logger.info(f"get place by id: {pk}")
    context = {'place': place}

    logger.info(f"get memory page -> '/memory/{pk}/'")
    return render(request, 'memories/memory.html', context)


# create memory
@login_required
def create_place(request):
    my_form = RawPlaceForm()

    if request.method == 'POST':
        my_form = RawPlaceForm(request.POST)

        if my_form.is_valid():
            Place.objects.create(**my_form.cleaned_data, user_id=request.user.id)
            return redirect('memories:memories')

        else:
            logger.warning("one or more fields have an error")

    context = {'form': my_form}
    return render(request, 'memories/map.html', context)


@login_required
def delete(request, pk):
    obj = get_object_or_404(Place, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('memories:memories')
    return render(request, 'memories/memories.html', {'obj': obj})
