from django.forms import ModelForm
from django import forms
from models import Profil, categorie_choices
from django.forms.widgets import CheckboxSelectMultiple


class ProfileForm(forms.ModelForm):
    categorie = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-group'}), choices=categorie_choices)

    class Meta:
        model = Profil
        fields = '__all__'
