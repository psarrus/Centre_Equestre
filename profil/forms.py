from django.forms import ModelForm
from models import Profil


class ProfilForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['civilite', 'nom', 'prenom', 'email', 'adresse', 'cp', 'ville', 'tel', 'mobile', 'siret']
