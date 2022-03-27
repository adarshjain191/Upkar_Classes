from django.contrib import admin
from django.urls import path
from main import views

admin.site.site_header = "Upakr Class Admin"
admin.site.site_title = "Upakr Class Admin Portal"
admin.site.index_title = "Welcome to Upkar Class Portal"

urlpatterns = [
    path("",views.home),
    path("ContactUs",views.ContactUs,name="Contactpage"),
    path("AboutUs",views.AboutUs,name="Aboutpage"),
    path("Resources",views.Resources,name="Resources"),
    path('admin/',admin.site.urls),
    path("Blog",views.Blog,name="Blog"),
    path("review",views.review,name="review")
]