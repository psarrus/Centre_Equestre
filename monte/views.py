from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from json_views.views import JSONListView, JSONFormView, JSONDataView, PaginatedJSONListView
from models import *
from django.contrib.auth.models import User
from profil.models import Profil

from forms import PiquetMontoirForm, CreneauMontoirEnseignantForm, PiquetMontoirReelForm, CreneauMontoirPrevisionnelForm


class CreneauMontoirCreate(CreateView):
    template_name = 'creneau_montoir_create.html'
    form_class = CreneauMontoirPrevisionnelForm
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
    queryset = CreneauMontoir.objects.all()
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

class CreneauMontoirReelCreate(CreateView):
    model = CreneauMontoirEnseignant
    form_class = CreneauMontoirEnseignantForm
    template_name = 'creneau_montoir_reel_create.html'
    success_url = reverse_lazy('piquet_reel_list')

    def dispatch(self, *args, **kwargs):
        self.creneau =  CreneauMontoir.objects.get(id=kwargs["pk_prev"])
        return super(CreneauMontoirReelCreate, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        form_kwargs = super(CreneauMontoirReelCreate, self).get_form_kwargs()
        form_kwargs.update({
            "initial" : {
                "date" : date.today(),
                "encadrant" : self.request.user.profile,
                "creneau_montoir" : self.creneau
            }
        })
        return form_kwargs

    def form_valid(self, form):
        #on copie le request.POST car on va y rajouter les champs date et encadrant qui ne sont pas present dans le formulaire et donc pas dans le request.POST
        post_data = self.request.POST.copy()
        if form.is_valid():
            self.object = creneau_montoir_enseignant = form.save()
            for piquet_montoir_staff in self.creneau.piquet_staff.all():
                #on rajoute le info de date et d encadrant provenant de piquet_montoir_staff car pas presente dans le formulaire
                post_data.update({
                    "piquet_montoir_reel_form_%s-date" % piquet_montoir_staff.id : creneau_montoir_enseignant.date,
                    "piquet_montoir_reel_form_%s-montoir" % piquet_montoir_staff.id : creneau_montoir_enseignant.id,
                })
                #on reconstruit les PiquetMontoirReelForm soumis en POST en utilisant bien le meme prefix
                piquet_montoir_reel_form = PiquetMontoirReelForm(post_data,
                                                                 prefix="piquet_montoir_reel_form_%s" %  piquet_montoir_staff.id)

                if piquet_montoir_reel_form.is_valid():
                    piquet_montoir_reel_form.save()
                else:
                    print piquet_montoir_reel_form.errors
            return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))


    def get_context_data(self, **kwargs):
        context = super(CreneauMontoirReelCreate, self).get_context_data(**kwargs)
        context['creneau'] = self.creneau
        context['date'] =  date.today()
        context['encadrant'] = self.request.user.profile

        context['piquet_montoir_reel_forms'] = []
        for piquet_montoir_staff in self.creneau.piquet_staff.all():
            #on cree un formulaire PiquetMontoirReelForm par piquet_montoir_staff, pre-initialise avec les donnees de piquet_montoir_staff
            #chaque PiquetMontoirReelForm a un prefix unique pour pouvoir etre reconstruit dans le form_valid
            piquet_montoir_reel_form = PiquetMontoirReelForm(prefix="piquet_montoir_reel_form_%s" %  piquet_montoir_staff.id, initial={
                "cheval" : piquet_montoir_staff.cheval,
                "selected" : piquet_montoir_staff.selected
            })

            piquet_montoir_reel_form.nom_cheval = piquet_montoir_staff.cheval.nom
            piquet_montoir_reel_form.aptitude = piquet_montoir_staff.cheval.get_aptitude_display
            piquet_montoir_reel_form.emplacement = piquet_montoir_staff.cheval.emplacement
            piquet_montoir_reel_form.id = piquet_montoir_staff.id

            profil_ids = self.creneau.public.periode_set.filter(fin__isnull=True).values_list("profil", flat=True)
            profils = Profil.objects.filter(id__in=profil_ids)
            piquet_montoir_reel_form.fields["profil"].queryset = profils

            context['piquet_montoir_reel_forms'].append(piquet_montoir_reel_form),

            print piquet_montoir_staff.id
        return context

class PiquetReelList(ListView):
    model = PiquetMontoirEnseignant
    template_name = 'piquet_montoir_reel_list.html'
    context_object_name = 'piquets'

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
