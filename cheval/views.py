from django.shortcuts import render
from django.views.generic.edit import CreateView
from models import Cheval


def cheval(request):
    return render(request,'cheval.html')


class ChevalCreate(CreateView):
    model = Cheval
    fields = ['sire','nom','race','pedigree','annee_naissance','photo','embouchure','enrennement','ferrage','remarques']
