from django.forms import ModelForm
from models import Cheval


class ChevalForm(ModelForm):
    class Meta:
        model = Cheval
        fields = ['sire','nom','race','pedigree','annee_naissance','photo','embouchure','enrennement','ferrage','remarques']
