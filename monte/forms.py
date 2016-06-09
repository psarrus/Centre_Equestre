from django import forms
from models import PiquetMontoirStaff, CreneauMontoirEnseignant

class PiquetMontoirForm(forms.ModelForm):
    class Meta:
        model = PiquetMontoirStaff
        fields = '__all__'

class CreneauMontoirEnseignForm(forms.ModelForm):
    class Meta:
        model = CreneauMontoirEnseignant
        fields = '__all__'
