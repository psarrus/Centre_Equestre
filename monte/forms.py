from django import forms
from models import *

class PiquetMontoirForm(forms.ModelForm):
    class Meta:
        model = PiquetMontoirStaff
        fields = '__all__'

class PiquetMontoirReelForm(forms.ModelForm):
    class Meta:
        model = PiquetMontoirEnseignant
        fields = '__all__'

class CreneauMontoirEnseignantForm(forms.ModelForm):
    class Meta:
        model = CreneauMontoirEnseignant
        fields = '__all__'
