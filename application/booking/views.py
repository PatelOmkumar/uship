from django.shortcuts import render,redirect
from .forms import Bookingforms
from .models import Booking

# Create your views here.
# def index(request):
#     forms = Bookingforms
#     return render(request,"booking/index.html",{'forms':forms})

def index(request):
    forms = Bookingforms(request.POST)
    if request.method == "POST":
        if forms.is_valid():
           forms.save()
           return redirect('booking')
        else:
           print("error while inserting data")
    return render(request,"booking/index.html",{'forms':forms})


def scrapbooking(request):
    forms = Bookingforms(request.POST)
    if request.method == "POST":
        if forms.is_valid():
           forms.save()
           return redirect('scrapbooking')
        else:
           print("error while inserting data")
    return render(request,"booking/scrapbooking.html",{'forms':forms})
