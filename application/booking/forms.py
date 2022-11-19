from django import forms
from .models import Booking

class Bookingforms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        # fields = ['from_place','To_place','moving_date','mes']
        widgets = {
            'from_place':forms.TextInput(attrs={'class':'text-input','title':'Enter Your Source','id':'from_place'}),
            'To_place':forms.TextInput(attrs={'class':'text-input','title':'Enter Your Destination','id':'To_place'}),
            'moving_date':forms.TextInput(attrs={'class':'text-input','title':'Enter Your Moving Date(dd/mm/yyyy)','id':'moving_date'}),
            'mes':forms.Textarea(attrs={'class':'text-input','title':'Enter Your Message','id':'mes'}),
        }