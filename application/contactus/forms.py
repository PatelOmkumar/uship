from django import forms
from .models import ContactUs_TB

class ContactUsForms(forms.ModelForm):
    class Meta:
        model = ContactUs_TB
        fields = ('First_name','Last_name','Email','Subject','Mesg')
        widgets = {
            'First_name':forms.TextInput(attrs={'class':'text-input','title':'Enter Your First Name','id':'fname'}),
            'Last_name':forms.TextInput(attrs={'class':'text-input','title':'Enter Your Last Name','id':'lname'}),
            'Email':forms.EmailInput(attrs={'class':'text-input','title':'Provide Email ID with lower case\nMust contain @ and . symbols\n\nFor Example:deepika@gmail.com','id':'email'}),
            'Subject':forms.TextInput(attrs={'class':'text-input','title':'Enter Your Subject','id':'subject'}),
            'Mesg':forms.Textarea(attrs={'class':'text-input','title':'Enter Your Query or Message','id':'message'})
        }