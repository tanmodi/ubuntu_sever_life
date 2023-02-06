from django.db import models

# Create your models here.
class search(models.Model):
    name = models.CharField(max_length=250,blank=True)
    address = models.CharField(max_length=250,blank=True)
    email = models.CharField(max_length=500,blank=True)
    phone = models.CharField(max_length=250,blank=True)
    map = models.CharField(max_length=500,blank=True)
    city = models.CharField(max_length=250,blank=True)
