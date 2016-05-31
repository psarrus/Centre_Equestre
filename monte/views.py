from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from json_views.views import JSONDetailView


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
    context_object_name = 'creneau'
    template_name = 'creneau_montoir_detail.html'
    #
    #
    # def get_context_data(self, **kwargs):
    #     context = super(CreneauMontoirDetail, self).get_context_data(**kwargs)
    #     context['creneau'] = self.get_object()
    #     context['chevaux'] = self.get_object().piquetmontoirstaff_set.all()
    #     context['form'] = PiquetMontoirForm()
    #
    #     return context


# class PiquetMontoirStaffUpdate(UpdateView):
#     model = PiquetMontoirStaff
#     fields = "__all__"
#     success_url = reverse_lazy('creneau_montoir_list')
#
#     def get_context_data(self, **kwargs):
#         context = super(CreneauMontoirDetail, self).get_context_data(**kwargs)
#         context['creneau'] = self.get_object()
#         context['chevaux'] = self.get_object().piquetmontoirstaff_set.all()
#         context['form'] = PiquetMontoirForm()
#
#         return context


class PiquetDetailJsonView(JSONDetailView):
    
    model = PiquetMontoirStaff
