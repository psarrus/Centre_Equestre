# -*- coding: utf-8 -*-
from django import forms
from models import Cheval, Journal, Emplacement


class ChevalForm(forms.ModelForm):
    class Meta:
        model = Cheval
        fields = ['sire', 'nom', 'race', 'pedigree', 'annee_naissance', 'photo', 'activite', 'remarques', 'statut', 'aptitude', 'emplacement']
        labels = {
            'sire':             'Numéro SIRE',
            'annee_naissance':  'Année de naissance',
            'activite':         'Activité pratiquée',
        }
        widgets = {
            'sire':             forms.TextInput(attrs={'class': 'form-control'}),
            'nom':              forms.TextInput(attrs={'class': 'form-control'}),
            'race':             forms.TextInput(attrs={'class': 'form-control'}),
            'pedigree':         forms.TextInput(attrs={'class': 'form-control'}),
            'annee_naissance':  forms.TextInput(attrs={'class': 'form-control'}),
            'activite':         forms.Select(attrs={'class': 'form-control'}),
            'remarques':        forms.TextInput(attrs={'class': 'form-control'}),
            'statut':           forms.Select(attrs={'class': 'form-control'}),
            'aptitude':         forms.Select(attrs={'class': 'form-control'}),
            'emplacement':      forms.Select(attrs={'class': 'form-control'}),
        }


class AptitudeForm(forms.ModelForm):
    class Meta:
        model = Cheval
        fields = ['aptitude']
        widgets = {
            'aptitude': forms.Select(attrs={'class': 'form-control'}),
        }


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = '__all__'
        widgets = {
            'cheval':   forms.Select(attrs={'class': 'form-control'}),
            'date':     forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motif':    forms.TextInput(attrs={'class': 'form-control'}),
            'lieu':     forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmplacementForm(forms.ModelForm):
    class Meta:
        model = Emplacement
        fields = '__all__'
        widgets = {
            'zone': forms.TextInput(attrs={'class': 'form-control'}),
            'box':  forms.TextInput(attrs={'class': 'form-control'}),
        }
