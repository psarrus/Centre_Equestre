from django.shortcuts import render, redirect
from models import Profil, Public, Periode
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from forms import ProfileForm


class CreateProfil(CreateView):
    model = ProfileForm
    form_class = ProfileForm
    template_name = 'create_profil.html'
    success_url = reverse_lazy('list_profil')


class ListProfil(ListView):
    model = Profil
    template_name = "list_profil.html"
    context_object_name = "profils"
    queryset = Profil.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListProfil, self).get_context_data(**kwargs)
        context.update({
            'periode': Periode.objects.all(),
        })
        return context


class ProfilUpdate(UpdateView):
    model = Profil
    fields = '__all__'
    template_name = 'profil_update.html'
    success_url = reverse_lazy('list_profil')

    def get_context_data(self, **kwargs):
        context = super(ProfilUpdate, self).get_context_data(**kwargs)
        context.update({
            'periode': Periode.objects.all(),
        })
        return context


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
