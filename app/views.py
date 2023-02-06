from django.shortcuts import render,redirect
from .models import Contact,newsletters
from speakerlogin.models import sUser
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core import serializers
from django.core.mail import send_mail
# Create your views here.



def page4(request):
    return render(request,'contact.html')
def page13(request):
    return render(request,'faq.html')
def page6(request):
    return render(request,'gallery.html')
def page7(request):
    context= {
	"user" : sUser.objects.all(),
	}
    return render(request,'index-2.html',context)
def page8(request):
    return render(request,'about.html')
def page1(request):
    context= {
	"user" : sUser.objects.all(),
	}
    return render(request,'index-2.html',context)
def page9(request):
    return render(request,'schedule-tab.html')
def page11(request):
    context= {
	"user" : sUser.objects.all(),
	}
    return render(request,'speakers-grid.html',context)

def Contactus(request):
    data = Contact()
    data.name = request.POST.get('name')
    data.email = request.POST.get('email')
    data.subject = request.POST.get('subject')
    data.message = request.POST.get('message')
    data.save()
    subject = 'Thanks ' + str(request.POST.get('name')) + ' for contact'
    body ="to " + str(request.POST.get('name')) + "\n We will soon contact you \n Thanks & Regards \n Life events team"
    email = request.POST.get('email')
    send_mail(
    subject,
    body,
    'lifeevent2023@outlook.com',
    [
    email
    ],
    fail_silently=False)
    return redirect('page1')
def newsletter(request):
    data = newsletters()
    data.email = request.POST.get('email')
    data.save()
    subject = ('you subscribed for newsletter')
    body = ('''you subscribed for newsletter
    you weekly get the notification
    please don't reply to this mail''')
    email = request.POST.get('email')
    send_mail(
    subject,
    body,
    'lifeevent2023@outlook.com',
    [
    email
    ],
    fail_silently=False)
    return redirect('page1')
