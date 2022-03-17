from django.shortcuts import render
from django.http import HttpResponse
from main.models import Contact,Announcements
from django.contrib import messages

def home(request):
    l=Announcements.objects.all()
    return render(request,"Home.html",{"l":l})
def AboutUs(request):
    return render(request,"About.html")
def ContactUs(request):
    if request.method=="POST":
        Name=request.POST.get("Name")
        Email=request.POST.get("Email")
        PhoneNumber=request.POST.get("PhoneNumber")
        Class=request.POST.get("Class")
        Feedback=request.POST.get("Feedback")
        contact=Contact(Name=Name,Email=Email,PhoneNumber=PhoneNumber,Class=Class,Feedback=Feedback)
        contact.save()
        messages.success(request,'Our team will contact you soon...')
    return render(request,"Contact.html")
def Resources(request):
    return render(request, "Resources.html")