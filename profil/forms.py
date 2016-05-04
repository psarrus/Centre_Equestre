from django.forms import ModelForm
from models import Profil
from django.contrib.auth.models import User


class ProfilForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['civilite', 'adresse', 'cp', 'ville', 'tel', 'mobile']
