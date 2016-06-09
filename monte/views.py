from django.shortcuts import render, redirect
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from json_views.views import JSONListView, JSONFormView, JSONDataView, PaginatedJSONListView

from models import *
from django.contrib.auth.models import User
from profil.models import Profil

from forms import PiquetMontoirForm, CreneauMontoirEnseignForm


class CreneauMontoirCreate(CreateView):
    model = CreneauMontoir
    fields = ['jour','heure_debut','duree','public','effectif','encadrant','remarque']
    template_name = 'creneau_montoir_create.html'
    success_url = reverse_lazy('creneau_montoir_previsonnel_list')

class CreneauMontoirPrevisionnelList(ListView):
    model = CreneauMontoir
    template_name = 'creneau_montoir_previsionnel_list.html'
    context_object_name = 'creneaux'
    queryset = CreneauMontoir.objects.all()

class CreneauMontoirReelList(ListView):
    model = CreneauMontoir
    template_name = 'creneau_montoir_reel_list.html'
    context_object_name = 'creneaux'
    queryset = CreneauMontoir.objects.filter(encadrant=4)
    def get_context_data(self, **kwargs):
        context = super(CreneauMontoirReelList, self).get_context_data(**kwargs)
        context['date_du_jour'] = date.today()
        # context['creneaux_encadrants'] = CreneauMontoir.objects.filter(encadrant=4)
        return context

class CreneauMontoirUpdate(UpdateView):
    model = CreneauMontoir
    fields = "__all__"
    template_name = 'creneau_montoir_update.html'
    success_url = reverse_lazy('creneau_montoir_previsonnel_list')

class CreneauMontoirDelete(DeleteView):
    model = CreneauMontoir
    template_name = 'creneau_montoir_delete.html'
    success_url = reverse_lazy('creneau_montoir_previsonnel_list')

class CreneauMontoirPrevisionnelDetail(DetailView):
    model = CreneauMontoir
    context_object_name = 'creneau'
    template_name = 'creneau_montoir_previsionnel_detail.html'

class CreneauMontoirReelDetail(DetailView):
    model = CreneauMontoir
    context_object_name = 'creneau'
    template_name = 'creneau_montoir_reel_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CreneauMontoirReelDetail, self).get_context_data(**kwargs)
        if not PiquetMontoirEnseignant.objects.all():
            print "ok"
            liste_piquet = PiquetMontoirStaff.objects.all()
        else:
            liste_piquet = CreneauMontoir.piquet_enseignant.filter(date = datetime.date.today())
            if not liste_piquet:
                liste_piquet = CreneauMontoir.piquet_staff.all
        context['liste_piquet'] = liste_piquet
        return context

# class CreneauMontoirReelDetail(DetailView):
#     model = CreneauMontoir
#     context_object_name = 'creneau'
#     template_name = 'creneau_montoir_reel_detail.html'

class CreneauMontoirEnseignantCreate(FormView):
    form_class = CreneauMontoirEnseignForm
    template_name = 'creneau_montoir_enseignant_create.html'
    success_url = reverse_lazy('piquet_montoir_reel')


class PiquetMontoirJsonListView(JSONListView):
    model = PiquetMontoirStaff


class PiquetMontoirJsonUpdateView(JSONFormView):
    form_class = PiquetMontoirForm

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(PiquetMontoirJsonUpdateView,self).dispatch(request, *args, **kwargs)

    def get_form(self):
        return PiquetMontoirForm(self.request.POST, instance=self.piquet_staff)

    def form_valid(self, form):
        piquet_staff = form.save()
        return self.render_to_response(self.get_context_data(success=True, piquet_staff=piquet_staff, form=form))

    def post(self, request, *args, **kwargs):
        self.piquet_staff=PiquetMontoirStaff.objects.get(id=kwargs["pk"])
        return super(PiquetMontoirJsonUpdateView,self).post(request, *args, **kwargs)
