from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import Cheval, Emplacement
from sante.models import RegistreSoins


class ChevalList(ListView):
    model = Cheval
    template_name = 'cheval_list.html'
    context_object_name = 'chevaux'
    queryset = Cheval.objects.all()


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

    def get_context_data(self, **kwargs):
        context = super(ChevalEtat, self).get_context_data(**kwargs)
        context["ferrage"] = RegistreSoins.objects.order_by("-date").get(acte=4)
        context["vermifugation"] = RegistreSoins.objects.order_by("-date").get(acte=3)
        context["soins"] = RegistreSoins.objects.order_by("-date").first()
        return context


class EmplacementList(ListView):
    model = Emplacement
    template_name = 'emplacement_list.html'
    context_object_name = 'emplacements'
    queryset = Emplacement.objects.all()


class EmplacementCreate(CreateView):
    model = Emplacement
    fields = ['zone','box']
    template_name = 'emplacement_create.html'
    success_url = reverse_lazy('emplacement_list')


class EmplacementDetail(DetailView):
    model = Emplacement
    template_name = 'emplacement_detail.html'
    context_object_name = 'emplacement'


class EmplacementUpdate(UpdateView):
    model = Emplacement
    fields = ['zone','box']
    template_name = 'emplacement_update.html'
    success_url = reverse_lazy('emplacement_list')


class EmplacementDelete(DeleteView):
    model = Emplacement
    template_name = 'emplacement_delete.html'
    success_url = reverse_lazy('emplacement_list')
