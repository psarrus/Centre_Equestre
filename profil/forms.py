from django.forms import ModelForm, modelform_factory
from django.forms.models import inlineformset_factory
from models import Profil, Periode

ProfilLineFormSet = inlineformset_factory(Profil, Periode,
                                            fields='__all__',
                                            extra=3)
