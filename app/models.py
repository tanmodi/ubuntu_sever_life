from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    name = models.CharField(max_length=250,blank=True)
    subject = models.CharField(max_length=250,blank=False)
    email = models.CharField(max_length=250,blank=False)
    message = models.CharField(max_length=250,blank=False)
    class meta:
        db_table = 'Contact'
class newsletters(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    email = models.CharField(max_length=250,blank=True)
