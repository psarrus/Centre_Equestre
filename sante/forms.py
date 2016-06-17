from django import forms
from models import Soin


class SoinForm(forms.ModelForm):
    class Meta:
        model = Soin
        fields = '__all__'
        widgets = {
            'date':         forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cheval':       forms.Select(attrs={'class': 'form-control'}),
            'pathologie':   forms.TextInput(attrs={'class': 'form-control'}),
            'acte':         forms.Select(attrs={'class': 'form-control'}),
            'soigneur':     forms.Select(attrs={'class': 'form-control'}),
        }
