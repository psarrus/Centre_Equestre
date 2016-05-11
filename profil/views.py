from django.shortcuts import render, redirect
from models import Profil, Public
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy


# def create_profil(request):
#     profils = Profil.objects.all()
#     if request.method =="POST":
#         profil_form = ProfilForm(request.POST)
#         if profil_form.is_valid():
#             profil_form.save()
#             # return render(request, "profil.html", {'form':profil_form})
#         return redirect("/profil")
#     else:
#         profil_form = ProfilForm()
#     return render(request, "profil.html", {'form':profil_form, 'profils':profils},)


class CreateProfil(CreateView):
    model = Profil
    fields = '__all__'
    template_name = 'create_profil.html'
    success_url = reverse_lazy('list_profil')


class ListProfil(ListView):
    model = Profil
    template_name = "list_profil.html"
    context_object_name = "profils"
    queryset = Profil.objects.all()


class ProfilUpdate(UpdateView):
    model = Profil
    fields = '__all__'
    template_name = 'profil_update.html'
    success_url = reverse_lazy('list_profil')


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


# def edit_profil(request, id):
#     profils = Profil.objects.all()
#     p = Profil.objects.get(id=id)
#     if request.method == "POST":
#         profil_form = ProfilForm(request.POST, instance=p)
#         if profil_form.is_valid():
#             profil_form.save()
#             return redirect("/vue_profil/%s" % id)
#     else:
#         profil_form = ProfilForm(instance=p)
#
#     return render(request,"profil.html",{'form':profil_form, 'profils':profils},)
