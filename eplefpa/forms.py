from django.forms import ModelForm

from models import Profil, Cheval

class ProfilForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['civilite', 'nom', 'prenom', 'adresse', 'cp', 'ville', 'tel', 'mobile', 'mail']

class ChevalForm(ModelForm):
    class Meta:
        model = Cheval
        fields = ['sire','nom','race','pedigree','annee_naissance','photo','embouchure','enrennement','ferrage','remarques']
