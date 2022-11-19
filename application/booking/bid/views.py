from django.shortcuts import render
from .forms import BidForms
from .models import bid

# Create your views here.
def index(request):
    objec = bid.objects.all()
    return render(request,"bid/index.html",{'objec':objec})

def post(request):
    objec = bid.objects.all()
    return render(request,"post/index.html",{'objec':objec})