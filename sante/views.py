from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from models import Soin


class SoinList(ListView):
    model = Soin
    template_name = 'soin_list.html'
    context_object_name = 'soins'


class SoinCreate(CreateView):
    model = Soin
    fields = '__all__'
    template_name = 'soin_create.html'
    success_url = reverse_lazy('soin_list')


class SoinDetail(DetailView):
    model = Soin
    template_name = 'soin_detail.html'
    context_object_name = 'soin'


class SoinUpdate(UpdateView):
    model = Soin
    fields = ['cheval', 'pathologie', 'acte', 'soigneur']
    template_name = 'soin_update.html'
    success_url = reverse_lazy('soin_list')
