from django.shortcuts import render,redirect
from .models import blogdetail,comments
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def blog(request):
	context= {
	"blogs" : blogdetail.objects.all(),
	"comments" : comments.objects.all(),
	}
	return render(request,'blog.html',context)

def reply(request):
	'''
	data = comments()
	data.name = request.POST['name']
	data.comment = request.POST['comment']
	data.image = request.POST['image']
	date = now
	data.save()
	'''
	now = datetime.datetime.now()
    #data.save()
	tanmay = request.FILES['image']
	user = comments.objects.create(name=request.POST['name'], content=request.POST['comment'], image=tanmay, date=now)
	user.save()
	return redirect('blog')
	context= {
	"blogs" : blogdetail.objects.all(),
	"comments" : comments.objects.all(),
	}
	return render(request,'blog.html',context)
