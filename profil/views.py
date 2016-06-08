from django.shortcuts import render, redirect
from models import Profil, Public, Periode
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import ProfilLineFormSet
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class CreateProfil(CreateView):
    model = Profil
    fields = ['civilite', 'nom', 'prenom', 'email', 'adresse', 'cp', 'ville', 'tel_1', 'tel_2', 'tel_3', 'profil_actif', 'permis']
    template_name = 'create_profil.html'
    success_url = reverse_lazy('list_profil')

    def get_context_data(self, **kwargs):
        context = super(CreateProfil, self).get_context_data(**kwargs)
        context ["profilline_formset"] = ProfilLineFormSet()
        return context

    def form_valid(self, form):
        profilline_formset = ProfilLineFormSet(self.request.POST)
        if form.is_valid() and profilline_formset.is_valid():
            profil = form.save()
            profilline_formset = ProfilLineFormSet(self.request.POST, instance=profil)
            profilline_formset.is_valid()
            profilline_formset.save()
            return redirect(reverse('list_profil'))
        return self.render_to_response(self.get_context_data(form=form))



class ListProfil(ListView):
    model = Profil
    template_name = "list_profil.html"
    context_object_name = "profils"
    queryset = Profil.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListProfil, self).get_context_data(**kwargs)
        context['periodes'] = Periode.objects.all()
        return context


class ProfilUpdate(UpdateView):
    model = Profil
    fields = ['civilite', 'nom', 'prenom', 'email', 'adresse', 'cp', 'ville', 'tel_1', 'tel_2', 'tel_3', 'profil_actif']
    template_name = 'profil_update.html'
    success_url = reverse_lazy('list_profil')

    def get_context_data(self, **kwargs):
        context = super(ProfilUpdate, self).get_context_data(**kwargs)
        context ["periodes"] = ProfilLineFormSet(instance=self.get_object())
        return context

    def form_valid(self, form):
        profilline_formset = ProfilLineFormSet(self.request.POST, instance=self.get_object())
        if form.is_valid() and profilline_formset.is_valid():
            profil = form.save()
            #(Des)Activation du User
            profil.user.is_active = profil.profil_actif
            profil.user.save()
            profilline_formset.save()
            return redirect(reverse('list_profil'))
        return self.render_to_response(self.get_context_data(form=form))

# =====================================================


class CreatePublic(CreateView):
    model = Public
    fields = '__all__'
    template_name = 'create_public.html'
    success_url = reverse_lazy('list_public')


class ListPublic(ListView):
    model = Public
    template_name = "list_public.html"
    context_object_name = "publics"
    queryset = Public.objects.all()


class PublicUpdate(UpdateView):
    model = Public
    fields = '__all__'
    template_name = 'public_update.html'
    success_url = reverse_lazy('list_public')
