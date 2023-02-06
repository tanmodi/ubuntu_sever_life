from django.db import models
from datetime import datetime
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class blogdetail(models.Model):
	heading = models.CharField(max_length=100)
	image = models.ImageField(upload_to='back_pics/')
	content = models.CharField(max_length=1000)
	date_posted = models.DateTimeField(default=datetime.now)

class comments(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='comments')
	content = models.CharField(max_length=1000)
	date = models.DateTimeField(default=datetime.now)
