from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from models import Profil, Cheval
from forms import ProfilForm

# Create your views here.
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

def cheval(request):
    return render(request,'cheval.html')


class ChevalCreate(CreateView):
    model = Cheval
    fields = ['sire','nom','race','pedigree','annee_naissance','photo','embouchure','enrennement','ferrage','remarques']

def encadrement(request):
    return render(request,'encadrement.html')

def homepage(request):
    return render(request,'homepage.html')
