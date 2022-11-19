from django.shortcuts import render
from .forms import ComplaintForms
from .models import Complaints_TB

# Create your views here.

def index(request):
    forms = ComplaintForms(request.POST)
    if forms.is_valid():
        forms.save()
    else:
        print("error")
    return render(request,"complaint/index.html",{'forms':forms})

def viewData(request):
    objec = Complaints_TB.objects.all()
    return render(request,"complaint/user.html",{'objec':objec})