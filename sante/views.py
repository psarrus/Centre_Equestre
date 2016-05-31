from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from models import RegistreSoins


class SoinList(ListView):
    model = RegistreSoins
    template_name = 'soin_list.html'
    context_object_name = 'soins'


class SoinCreate(CreateView):
    model = RegistreSoins
    fields = '__all__'
    template_name = 'soin_create.html'
    success_url = reverse_lazy('soin_list')


class SoinDetail(DetailView):
    model = RegistreSoins
    template_name = 'soin_detail.html'
    context_object_name = 'soin'


class SoinUpdate(UpdateView):
    model = RegistreSoins
    fields = ['cheval', 'pathologie', 'acte', 'soigneur']
    template_name = 'soin_update.html'
    success_url = reverse_lazy('soin_list')
