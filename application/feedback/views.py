from django.shortcuts import render
from .forms import FeedbackForms
from .models import feedback_TB

# Create your views here.
def index(request):
    forms = FeedbackForms(request.POST)
    if forms.is_valid():
        forms.save()
    else:
        print("error")
    return render(request,"feedback/index.html",{'forms':forms})

def viewData(request):
    objec = feedback_TB.objects.all()
    return render(request,"feedback/user.html",{'objec':objec})