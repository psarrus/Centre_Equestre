from django import forms
from models import Cheval, Emplacement, Journal


class EmplacementForm(forms.ModelForm):
    class Meta:
        model = Emplacement
        fields = '__all__'


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = '__all__'


class AptitudeForm(forms.ModelForm):
    class Meta:
        model = Cheval
        fields = ['aptitude']
