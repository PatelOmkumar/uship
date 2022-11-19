from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="bid"),
    path('post/',views.post,name="post"),
    path('companybid/',views.companybid,name="companybid")
]
