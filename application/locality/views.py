from django.shortcuts import render
from .forms import StateForms,CityForms,AreaForms
from .models import state,city,area

# Create your views here.
def index(request):
    forms1 = StateForms(request.POST)
    forms2 = CityForms(request.POST)
    forms3 = AreaForms(request.POST)
    if forms1.is_valid():
        forms1.save()
        if forms2.is_valid():
            forms2.save()
            if forms3.is_valid():
                forms3.save()
            else:
                print("error form3")
        else:
            print("error form2")
    else:
        print("error form1")
    return render(request,"locality/index.html",{'forms1':forms1,'forms2':forms2,'forms3':forms3})

def viewData(request):
    objec1 = state.objects.all()
    objec2 = city.objects.all()
    objec3 = area.objects.all()
    return render(request,"locality/user.html",{'objec1':objec1,'objec2':objec2,'objec3':objec3})