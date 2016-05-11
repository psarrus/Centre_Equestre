from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from models import *


# def encadrement(request):
#     return render(request,'encadrement.html')
#
#
def homepage(request):
    return render(request,'homepage.html')



class CreneauMontoirCreate(CreateView):
    model = CreneauMontoir
    fields = ['jour','heure_debut','duree','classe','effectif','encadrant','remarque']
    template_name = 'creneau_montoir_create.html'
    success_url = reverse_lazy('homepage')


# class CreneauMontoirUpdate(UpdateView):
#     model = CreneauMontoir
#     fields = ['jour','heure_debut','duree','classe','effectif','encadrant','remarque']
#     template_name = 'creneau_montoir_update.html'
#     success_url = reverse_lazy('homepage')
#
#
#
#
# class PiquetMontoirStaffCreate(CreateView):
#     model = PiquetMontoirStaff
#     fields = ['montoir', 'cheval']
#     template_name = 'piquet_montoir_staff_create.html'
#     success_url = reverse_lazy('homepage')
#
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
