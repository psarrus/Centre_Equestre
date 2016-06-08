from django import forms
from models import PiquetMontoirStaff

class PiquetMontoirForm(forms.ModelForm):
    class Meta:
        model = PiquetMontoirStaff
        fields = '__all__'
        # fields = ['selected']
