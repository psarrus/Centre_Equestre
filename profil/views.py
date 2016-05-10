from django.shortcuts import render, redirect
from models import Profil
from forms import ProfilForm


def create_profil(request):
    profils = Profil.objects.all()
    if request.method =="POST":
        profil_form = ProfilForm(request.POST)
        if profil_form.is_valid():
            profil_form.save()
            # return render(request, "profil.html", {'form':profil_form})
        return redirect("/profil")
    else:
        profil_form = ProfilForm()
    return render(request, "profil.html", {'form':profil_form, 'profils':profils},)


def edit_profil(request, id):
    profils = Profil.objects.all()
    p = Profil.objects.get(id=id)
    if request.method == "POST":
        profil_form = ProfilForm(request.POST, instance=p)
        if profil_form.is_valid():
            profil_form.save()
            return redirect("/vue_profil/%s" % id)
    else:
        profil_form = ProfilForm(instance=p)

    return render(request,"profil.html",{'form':profil_form, 'profils':profils},)
