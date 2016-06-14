from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import Cheval, Emplacement, Journal
from forms import AptitudeForm, EmplacementForm, JournalForm


class ChevalList(ListView):
    model = Cheval
    template_name = 'cheval_list.html'
    context_object_name = 'chevaux'


class ChevalCreate(CreateView):
    model = Cheval
    fields = ['sire', 'nom', 'race', 'pedigree', 'annee_naissance', 'photo', 'activite', 'remarques', 'statut', 'aptitude', 'emplacement']
    template_name = 'cheval_create.html'
    success_url = reverse_lazy('cheval_list')


class ChevalDetail(DetailView):
    model = Cheval
    template_name = 'cheval_detail.html'
    context_object_name = 'cheval'


class ChevalUpdate(UpdateView):
    model = Cheval
    fields = ['sire', 'nom', 'race', 'pedigree', 'annee_naissance', 'photo', 'activite', 'remarques', 'statut', 'aptitude', 'emplacement']
    template_name = 'cheval_update.html'
    success_url = reverse_lazy('cheval_list')


class ChevalEtat(ListView):
    model = Cheval
    template_name = 'cheval_etat.html'
    context_object_name = 'chevaux'

    def get_context_data(self, **kwargs):
        context = super(ChevalEtat, self).get_context_data(**kwargs)
        chevaux = {}
        for cheval in self.get_queryset():
            chevaux[cheval] = AptitudeForm(instance = cheval)
        context['chevaux'] = chevaux
        context['form'] = AptitudeForm()
        return context


class AptitudeUpdate(UpdateView):
    model = Cheval
    fields = ['aptitude']
    success_url = reverse_lazy('cheval_etat')


class Emplacement(ListView):
    model = Emplacement
    template_name = 'emplacement.html'
    context_object_name = 'emplacements'

    def get_context_data(self, **kwargs):
        context = super(Emplacement,self).get_context_data(**kwargs)
        context['form'] = EmplacementForm()
        return context


class EmplacementCreate(CreateView):
    model = Emplacement
    form_class = EmplacementForm
    success_url = reverse_lazy('emplacement')


class EmplacementUpdate(UpdateView):
    model = Emplacement
    fields = '__all__'
    template_name = 'emplacement_update.html'
    success_url = reverse_lazy('emplacement')


class EmplacementDelete(DeleteView):
    model = Emplacement
    template_name = 'emplacement_delete.html'
    success_url = reverse_lazy('emplacement')


class Journal(ListView):
    model = Journal
    template_name = 'journal.html'
    context_object_name = 'journaux'

    def get_context_data(self, **kwargs):
        context = super(Journal,self).get_context_data(**kwargs)
        context['form'] = JournalForm()
        return context


class JournalCreate(CreateView):
    model = Journal
    form_class = JournalForm
    success_url = reverse_lazy('journal')


class JournalUpdate(UpdateView):
    model = Journal
    fields = '__all__'
    template_name = 'journal_update.html'
    success_url = reverse_lazy('journal')
