from django import forms
from django.forms import HiddenInput, TextInput, Textarea, Select
from models import *

class PiquetMontoirForm(forms.ModelForm):
    class Meta:
        model = PiquetMontoirStaff
        fields = '__all__'

class PiquetMontoirReelForm(forms.ModelForm):
    class Meta:
        model = PiquetMontoirEnseignant
        fields = '__all__'

        widgets = {
            'cheval': HiddenInput(),
        }

class CreneauMontoirEnseignantForm(forms.ModelForm):
    class Meta:
        model = CreneauMontoirEnseignant
        fields = '__all__'

class CreneauMontoirPrevisionnelForm(forms.ModelForm):
    class Meta:
        model = CreneauMontoir
        fields = '__all__'
        widgets = {
            'jour': Select(attrs={'placeholder':'Jour'}),
            'heure_debut': TextInput(attrs={'placeholder':'Heure de debut'}),
            'duree': TextInput(attrs={'placeholder':'Duree'}),
            'effectif': TextInput(attrs={'placeholder':'Effectif'}),
            'encadrant': TextInput(attrs={'placeholder':'Professeur'}),
            'remarque': Textarea(attrs={'placeholder':'Remarques'}),
            'public': Select(attrs={'placeholder':'Public'}),
        }
