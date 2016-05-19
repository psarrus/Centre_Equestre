from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import RegistreSoins

class SoinCreate(CreateView):
    model = RegistreSoins
    fields = '__all__'
    # fields = ['pathologie','acte','cheval','soigneur']
    template_name = 'soin_create.html'
    success_url = reverse_lazy('soins')


class SoinList(ListView):
    model = RegistreSoins
    template_name = 'soin.html'
    context_object_name = 'soins'
    queryset = RegistreSoins.objects.all()


class SoinDetail(DetailView):
    model = RegistreSoins
    template_name = 'soin_detail.html'
    context_object_name = 'soin'


class SoinUpdate(UpdateView):
    model = RegistreSoins
    fields = ['pathologie','acte','cheval','soigneur']
    template_name = 'soin_update.html'
    success_url = reverse_lazy('soins')


class SoinDelete(DeleteView):
    model = RegistreSoins
    template_name = 'soin_delete.html'
    success_url = reverse_lazy('soins')
