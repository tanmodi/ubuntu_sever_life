from django.db import models
from datetime import datetime
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class sUser(models.Model):
    name = models.CharField(max_length=250,blank=True)
    username = models.CharField(max_length=500,blank=True)
    email = models.CharField(max_length=250,blank=False)
    gender = models.CharField(max_length=250,blank=True)
    age = models.CharField(max_length=250,blank=False)
    city = models.CharField(max_length=250,blank=False)
    country = models.CharField(max_length=250,blank=False)
    mobileno = models.CharField(max_length=250,blank=True)
    password = models.CharField(max_length=250,blank=True)
    zipcode = models.CharField(max_length=250,blank=True)
    image = models.ImageField(upload_to='speaker',default="speaker/default.jpg")
    about = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
