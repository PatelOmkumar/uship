from django.urls import path
from . import views
from .views import PasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="mainpage"),
    path('home/',views.home,name="mainpage"),
    path('UserForm/',views.UserForm.as_view(),name="UserSignup"),
    path('CompanyForm/',views.CompanyForm.as_view(),name="CompanyForm"),
    path('login/',views.loginpage,name="loginpage"),
    path('resetpassword/',PasswordChangeView.as_view(template_name='dbmodels/resetpassword.html'),name="resetpassword"),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('about/',views.about,name="aboutUspage"),
    path('faq/',views.faq,name="faqpage"),
    path('howitworks/',views.howitworks,name="howitworks"),
    path('packersandmovers/',views.packersandmovers,name="packersandmoverspage"),
    path('scrapcollectors/',views.scrapcollectors,name="scrapcollectorspage"),
    path('bothpackersandmovers/',views.bothpackersandmovers,name="bothpackersandmoverspage"),
    path('logout_view/',views.logout_view,name="logout"),
    path('myaccount/',views.myaccount,name="myaccount"),
    path('mypost/',views.mypost,name="mypost"),
    path('mybookings/',views.mybookings,name="mybookings"),
    path('companyfeedback/',views.companyFeedback,name="companyfeedback"),
    path('companycomplaint/',views.companycomplaint,name="companycomplaint"),
    path('bidlist/',views.bidlist,name="bidlist"),
]
