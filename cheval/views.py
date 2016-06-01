from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import Cheval, Emplacement


class ChevalList(ListView):
    model = Cheval
    template_name = 'cheval_list.html'
    context_object_name = 'chevaux'


class ChevalCreate(CreateView):
    model = Cheval
    fields = ['sire','nom','race','pedigree','annee_naissance','photo','activite','remarques','statut','aptitude','emplacement']
    template_name = 'cheval_create.html'
    success_url = reverse_lazy('cheval_list')


class ChevalDetail(DetailView):
    model = Cheval
    template_name = 'cheval_detail.html'
    context_object_name = 'cheval'


class ChevalUpdate(UpdateView):
    model = Cheval
    fields = ['sire','nom','race','pedigree','annee_naissance','photo','activite','remarques','statut','aptitude','emplacement']
    template_name = 'cheval_update.html'
    success_url = reverse_lazy('cheval_list')


class ChevalEtat(ListView):
    model = Cheval
    template_name = 'cheval_etat.html'
    context_object_name = 'chevaux'


class EmplacementList(ListView):
    model = Emplacement
    template_name = 'emplacement_list.html'
    context_object_name = 'emplacements'


class EmplacementCreate(CreateView):
    model = Emplacement
    fields = '__all__'
    template_name = 'emplacement_create.html'
    success_url = reverse_lazy('emplacement_list')


class EmplacementDetail(DetailView):
    model = Emplacement
    template_name = 'emplacement_detail.html'
    context_object_name = 'emplacement'


class EmplacementUpdate(UpdateView):
    model = Emplacement
    fields = '__all__'
    template_name = 'emplacement_update.html'
    success_url = reverse_lazy('emplacement_list')


class EmplacementDelete(DeleteView):
    model = Emplacement
    template_name = 'emplacement_delete.html'
    success_url = reverse_lazy('emplacement_list')
