from django.shortcuts import render
from django.http import HttpResponse
from main.models import Contact
from django.contrib import messages

def home(request):
    # l=["I have a template songs.html that includes a child template addToPlaylist.html. I need the title of the song that is to be added to the playlist dynamically. Here is the code for songs.html which includes addToPlaylist.html.","@Moosa I want the value of song.title that I am iterating in parent. So I can add relevant song to the playlist user chooses. song.title should be the title of song for which addToPlaylist button is clicked."]
    return render(request,"Home.html")
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