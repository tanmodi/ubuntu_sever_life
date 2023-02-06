from django.contrib import admin
from .models import blogdetail
from .models import comments

# Register your models here.

admin.site.register(blogdetail)
admin.site.register(comments)
