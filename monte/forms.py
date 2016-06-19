from django import forms
from django.forms import HiddenInput, TextInput, Textarea, Select
from models import *
from profil.models import Periode, Profil

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
            # 'jour': Select(attrs={'placeholder':'Jour'}),
            'heure_debut': TextInput(attrs={'placeholder':'Heure de debut'}),
            'duree': TextInput(attrs={'placeholder':'Duree'}),
            'effectif': TextInput(attrs={'placeholder':'Effectif'}),
            # 'encadrant': Select(attrs={'placeholder':'Professeur'}, choices=profs_choices),
            'remarque': Textarea(attrs={'placeholder':'Remarques'}),
            'public': Select(attrs={'placeholder':'Public'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreneauMontoirPrevisionnelForm, self).__init__(*args, **kwargs)
        profil_ids = Periode.objects.filter(categorie="3", fin__isnull=True).values_list('profil', flat=True)
        profs = Profil.objects.filter(id__in=profil_ids)
        self.fields["encadrant"].queryset = profs
