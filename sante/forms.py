from django import forms
from models import Soin


class SoinForm(forms.ModelForm):
    class Meta:
        model = Soin
        fields = '__all__'
