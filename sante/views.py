from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from models import Soin
from forms import SoinForm


class SoinListView(ListView):
    model = Soin
    template_name = 'soin.html'
    context_object_name = 'soins'

    def get_context_data(self, **kwargs):
        context = super(SoinListView,self).get_context_data(**kwargs)
        context['form'] = SoinForm()
        return context


class SoinCreateView(CreateView):
    model = Soin
    form_class = SoinForm
    success_url = reverse_lazy('soin_list')


class SoinUpdateView(UpdateView):
    model = Soin
    form_class = SoinForm
    template_name = 'soin_update.html'
    success_url = reverse_lazy('soin_list')
