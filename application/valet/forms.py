from django import forms
from .models import Valet_Details_TB

class ValetForms(forms.ModelForm):
    class Meta:
        model = Valet_Details_TB
        fields = '__all__'
