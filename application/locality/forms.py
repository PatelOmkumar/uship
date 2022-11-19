from django import forms
from .models import state,city,area

class StateForms(forms.ModelForm):
    class Meta:
        model = state
        fields = '__all__'

class CityForms(forms.ModelForm):
    class Meta:
        model = city
        fields = '__all__'
    
class AreaForms(forms.ModelForm):
    class Meta:
        model = area
        fields = '__all__'
