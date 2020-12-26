from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .forms import PlaceModelForm, PlaceUpdateModelForm
from .models import Place
from django.db.models import Q


# get all places
class PlaceListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = 'memories/memories.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Place.objects.filter(user_id=self.request.user.id)
        return Place.objects.filter(name__icontains=query)

    def get_context_data(self, **kwargs):
        context = super(PlaceListView, self).get_context_data(**kwargs)
        context['places_quantity'] = Place.objects.filter(user_id=self.request.user.id).count()
        return context


# get place by id
class PlaceDetailView(LoginRequiredMixin, DetailView):
    model = Place
    template_name = 'memories/memory.html'


# create place
class PlaceCreateView(LoginRequiredMixin, CreateView):
    form_class = PlaceModelForm
    model = Place
    template_name = 'memories/map.html'
    success_url = reverse_lazy('memories:memories')

    def form_valid(self, form):
        form.instance.user = User.objects.get(id=self.request.user.id)
        return super(PlaceCreateView, self).form_valid(form)


# delete place
class PlaceDeleteView(LoginRequiredMixin, DeleteView):
    model = Place
    template_name = 'memories/memories.html'
    success_url = reverse_lazy('memories:memories')


# update place
class PlaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Place
    form_class = PlaceUpdateModelForm
    template_name = 'memories/update-form.html'
    success_url = reverse_lazy('memories:memories')

# class SearchPlaceListView(LoginRequiredMixin, ListView):
#     model = Place
#     template_name = 'memories/memories.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         print(f'query = {query}')
#         page_obj = Place.objects.filter(name__icontains=query)
#         return page_obj
