from django.shortcuts import render



# Create your views here.
def index(request):
    forms = FeedbackForms(request.POST)
    if forms.is_valid():
        forms.save()
    else:
        print("error")
    return render(request,"companyFeedback/index.html",{'forms':forms})

def viewData(request):
    objec = feedback_TB.objects.all()
    return render(request,"companyFeedback/user.html",{'objec':objec})