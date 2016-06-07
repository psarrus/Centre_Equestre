from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from json_views.views import JSONListView, JSONFormView, JSONDataView, PaginatedJSONListView
from django.views.decorators.csrf import csrf_exempt

from models import *

from forms import PiquetMontoirForm


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
