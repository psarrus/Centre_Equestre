from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from models import Cheval, Emplacement


class ChevalList(ListView):
    model = Cheval
    template_name = 'cheval.html'
    context_object_name = 'chevaux'
    queryset = Cheval.objects.all()


class ChevalCreate(CreateView):
    model = Cheval
    fields = ['sire','nom','race','pedigree','annee_naissance','photo','date_entree','activite','remarques','status','aptitude','emplacement']
    template_name = 'cheval_create_form.html'
    success_url = reverse_lazy('cheval_list')


class ChevalUpdate(UpdateView):
    model = Cheval
    fields = ['sire','nom','race','pedigree','annee_naissance','photo','date_entree','activite','remarques','status','aptitude','emplacement']
    template_name = 'cheval_update_form.html'
    success_url = reverse_lazy('cheval_list')


class EmplacementList(ListView):
    model = Emplacement
    template_name = 'emplacement.html'
    context_object_name = 'emplacements'
    queryset = Emplacement.objects.all()


class EmplacementCreate(CreateView):
    model = Emplacement
    fields = ['zone','box']
    template_name = 'emplacement_create_form.html'
    success_url = reverse_lazy('emplacement_list')


class EmplacementUpdate(UpdateView):
    model = Emplacement
    fields = ['zone','box']
    template_name = 'emplacement_update_form.html'
    success_url = reverse_lazy('emplacement_list')
