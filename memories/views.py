from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from .forms import PlaceModelForm
from .models import Place


# get all places
class PlaceListView(LoginRequiredMixin, ListView):
    model = Place
    paginate_by = 10
    template_name = 'memories/memories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(PlaceListView, self).get_context_data(**kwargs)
        object_list = Place.objects.filter(user_id=self.request.user.id)
        paginator = Paginator(object_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        contex['page_obj'] = page_obj
        return contex


# get place by id
class PlaceDetailView(LoginRequiredMixin, DetailView):
    model = Place
    context_object_name = 'place'
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
