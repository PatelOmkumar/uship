from django.shortcuts import render
from .forms import ValetForms
from .models import Valet_Details_TB

# Create your views here.
def index(request):
    forms = ValetForms(request.POST)
    if forms.is_valid():
        forms.save()
    else:
        print("error")
    return render(request,"valet/index.html",{'forms':forms})

def viewData(request):
    objec = Valet_Details_TB.objects.all()
    return render(request,"valet/user.html",{'objec':objec})