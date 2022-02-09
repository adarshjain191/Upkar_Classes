from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path("",views.home),
    path("ContactUs",views.ContactUs,name="Contactpage"),
    path("AboutUs",views.AboutUs,name="Aboutpage")
]