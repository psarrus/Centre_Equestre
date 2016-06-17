from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import Cheval, Journal, Emplacement
from forms import ChevalForm, AptitudeForm, JournalForm, EmplacementForm


class ChevalListView(ListView):
    model = Cheval
    template_name = 'cheval_list.html'
    context_object_name = 'chevaux'


class ChevalCreateView(CreateView):
    model = Cheval
    form_class = ChevalForm
    template_name = 'cheval_create.html'
    success_url = reverse_lazy('cheval_list')


class ChevalDetailView(DetailView):
    model = Cheval
    template_name = 'cheval_detail.html'
    context_object_name = 'cheval'


class ChevalUpdateView(UpdateView):
    model = Cheval
    form_class = ChevalForm
    template_name = 'cheval_update.html'
    success_url = reverse_lazy('cheval_list')


class ChevalEtatView(ListView):
    model = Cheval
    template_name = 'cheval_etat.html'
    context_object_name = 'chevaux'

    def get_context_data(self, **kwargs):
        context = super(ChevalEtatView, self).get_context_data(**kwargs)
        chevaux = {}
        for cheval in self.get_queryset():
            chevaux[cheval] = AptitudeForm(instance = cheval)
        context['chevaux'] = chevaux
        context['form'] = AptitudeForm()
        return context


class AptitudeUpdateView(UpdateView):
    model = Cheval
    form_class = AptitudeForm
    success_url = reverse_lazy('cheval_etat')


class EmplacementListView(ListView):
    model = Emplacement
    template_name = 'emplacement.html'
    context_object_name = 'emplacements'

    def get_context_data(self, **kwargs):
        context = super(EmplacementListView,self).get_context_data(**kwargs)
        context['form'] = EmplacementForm()
        return context


class EmplacementCreateView(CreateView):
    model = Emplacement
    form_class = EmplacementForm
    success_url = reverse_lazy('emplacement_list')


class EmplacementUpdateView(UpdateView):
    model = Emplacement
    form_class = EmplacementForm
    template_name = 'emplacement_update.html'
    success_url = reverse_lazy('emplacement_list')


class EmplacementDeleteView(DeleteView):
    model = Emplacement
    template_name = 'emplacement_delete.html'
    success_url = reverse_lazy('emplacement_list')


class JournalListView(ListView):
    model = Journal
    template_name = 'journal.html'
    context_object_name = 'journaux'

    def get_context_data(self, **kwargs):
        context = super(JournalListView,self).get_context_data(**kwargs)
        context['form'] = JournalForm()
        return context


class JournalCreateView(CreateView):
    model = Journal
    form_class = JournalForm
    success_url = reverse_lazy('journal_list')


class JournalUpdateView(UpdateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journal_update.html'
    success_url = reverse_lazy('journal_list')
