from django.db import models

# Create your models here.
class User(models.Model):
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

class Register(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    name = models.CharField(max_length=250,blank=True)
    email = models.CharField(max_length=250,blank=False)
    gender = models.CharField(max_length=250,blank=False)
    age = models.CharField(max_length=250,blank=False)
    state = models.CharField(max_length=250,blank=False)
    occupation = models.CharField(max_length=250,blank=False)
    class meta:
        db_table = 'Register'
