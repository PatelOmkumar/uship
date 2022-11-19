from django.shortcuts import render,redirect
from .forms import ContactUsForms
from .models import ContactUs_TB
# Create your views here.
def index(request):
    forms = ContactUsForms(request.POST)
    if forms.is_valid():
        forms.save()
        return redirect('contactus')
    else:
        forms = ContactUsForms()
    return render(request,"contactus/index.html",{'forms':forms},{'msg':"Thank You For Contacting us !"})