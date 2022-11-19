from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="addcomplaint"),
    path('viewData/',views.viewData,name="viewcomplaintdata"),
]
