from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="post"),
    path('viewallpost/',views.viewallpost,name="viewallpost")
]
