from django import forms
from models import PiquetMontoirStaff
from cheval.models import Cheval

class PiquetMontoirForm(forms.ModelForm):
    class Meta:
        model = PiquetMontoirStaff
        fields = ['cheval']
    # def __init__(self, *args, **kwargs):
    #      super(PiquetMontoirForm, self).__init__(**kwargs)
    #      self.fields['activite'].queryset = Cheval.objects.filter(activite="1")
        # widgets = {
        #     'chevaux': forms.CheckboxSelectMultiple,
        # }
