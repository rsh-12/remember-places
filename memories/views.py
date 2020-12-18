import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from .forms import RawPlaceForm
from .models import Place

logger = logging.getLogger(__name__)


class PlaceListView(LoginRequiredMixin, ListView):
    model = Place
    paginate_by = 10
    template_name = 'memories/memories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(PlaceListView, self).get_context_data(**kwargs)
        contex['page_obj'] = Place.objects.filter(user_id=self.request.user.id)
        return contex


class PlaceDetailView(LoginRequiredMixin, DetailView):
    model = Place
    context_object_name = 'place'
    template_name = 'memories/memory.html'


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


# delete place
class PlaceDeleteView(LoginRequiredMixin, DeleteView):
    model = Place
    template_name = 'memories/memories.html'
    success_url = reverse_lazy('memories:memories')
