from django.db import models

class Contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=50)
    PhoneNumber=models.CharField(max_length=12)
    Class=models.TextField(max_length=10)
    Feedback=models.TextField(max_length=500)

    def __str__(self):
        return self.Name+"-/-"+self.Email
    
class Announcements(models.Model):
    A=models.TextField(max_length="1000")

class Notes(models.Model):
    n=models.FileField(upload_to="doc")