from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from models import *
from cheval.models import Cheval

from forms import PiquetMontoirForm


def homepage(request):
    return render(request,'homepage.html')



class CreneauMontoirCreate(CreateView):
    model = CreneauMontoir
    fields = ['jour','heure_debut','duree','public','effectif','encadrant','remarque']
    template_name = 'creneau_montoir_create.html'
    success_url = reverse_lazy('creneau_montoir_list')

class CreneauMontoirList(ListView):
    model = CreneauMontoir
    template_name = 'creneau_montoir_liste.html'
    context_object_name = 'creneaux'
    queryset = CreneauMontoir.objects.all()

class CreneauMontoirUpdate(UpdateView):
    model = CreneauMontoir
    fields = "__all__"
    template_name = 'creneau_montoir_update.html'
    success_url = reverse_lazy('creneau_montoir_list')

class CreneauMontoirDelete(DeleteView):
    model = CreneauMontoir
    template_name = 'creneau_montoir_delete.html'
    success_url = reverse_lazy('creneau_montoir_list')


class CreneauMontoirDetail(DetailView):
    model = CreneauMontoir
    template_name = 'creneau_montoir_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CreneauMontoirDetail, self).get_context_data(**kwargs)
        context['creneau'] = self.get_object()
        context['chevaux'] = Cheval.objects.filter(activite="1")

        return context





class PiquetMontoirStaffCreate(FormView):
    model = PiquetMontoirStaff
    form_class = PiquetMontoirForm
    # fields = ['montoir', 'cheval']
    template_name = 'creneau_montoir_detail.html'
    success_url = reverse_lazy('piquet_montoir')





# class PiquetMontoirStaffUpdate(UpdateView):
#     model = PiquetMontoirStaff
#     fields = ['montoir', 'cheval']
#     template_name = 'piquet_montoir_staff_update.html'
#     success_url = reverse_lazy('homepage')
#
#
#
#
# class PiquetMontoirEnseignantCreate(CreateView):
#     model = PiquetMontoirEnseignant
#     fields = ['montoir', 'cheval', 'date', 'profil']
#     template_name = 'piquet_montoir_enseignant_create.html'
#     success_url = reverse_lazy('homepage')
#
# class PiquetMontoirEnseignantUpdate(UpdateView):
#     model = PiquetMontoirEnseignant
#     fields = ['montoir', 'cheval', 'date', 'profil']
#     template_name = 'piquet_montoir_enseignant_update.html'
#     success_url = reverse_lazy('homepage')
