from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from models import Cheval


class ChevalList(ListView):
    model = Cheval
    template_name = "cheval.html"
    context_object_name = "chevaux"
    queryset = Cheval.objects.all()


class ChevalCreate(CreateView):
    model = Cheval
    fields = ['sire','nom','race','pedigree','annee_naissance','photo','date_entree','activite','remarques','status','emplacement','aptitude']
    template_name = 'cheval_create_form.html'
    success_url = reverse_lazy('cheval_list')


class ChevalUpdate(UpdateView):
    model = Cheval
    fields = ['sire','nom','race','pedigree','annee_naissance','photo','date_entree','activite','remarques','status','emplacement','aptitude']
    template_name = 'cheval_update_form.html'
    success_url = reverse_lazy('cheval_list')
