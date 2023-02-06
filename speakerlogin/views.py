from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from .models import sUser
from blog.models import blogdetail,comments
from search.models import search
from django.contrib import messages
import bcrypt
import random
import requests
from django.core.mail import send_mail
from django.core import serializers
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
def smain(request):
    return render(request,'speakerlogin/sregister.html')
def suserregister(request):
    now = datetime.datetime.now()
    if (sUser.objects.filter(username=request.POST['username']).exists()):
        return redirect('smain')
    if (request.POST.get('password')!=request.POST.get('repassword')):
        return redirect('smain')
    
    user = sUser.objects.create(about=request.POST['about'], name=request.POST['name'], username=request.POST['username'], password=request.POST['password'], mobileno=request.POST['mobileno'],gender=request.POST['gender'],country=request.POST['country'],zipcode=request.POST['zipcode'],city=request.POST['city'],age=request.POST['age'],email=request.POST['email'],  image=request.FILES.get('images'), date=now)
    user.save()
    otpsms = 'Hey ' + str(request.POST['name']) + '\n' +  ' your registration is sucessfull ' + ' \nlife events '

    id = "TXTIND"
    # mobile_no = 
    senderid = "sender_id=" + id
    message = "&message=" + otpsms
    route = "&route=" + "v3"
    number = "&numbers=" + str(request.POST['mobileno'])
    # payload = "sender_id=TXTIND&message=This is a test message&route=v3&numbers=9354317075"
    
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = senderid + message + route + number
    headers = {
      'authorization': "kaGNdrFqnTuZQ0hINefJ7IWn1UL4VX9u9l6u4AkbK8t1gQLzEa7aCSkJ6uVh",
      'Content-Type': "application/x-www-form-urlencoded",
      'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    request.session['id'] = user.id
    name = request.POST.get('name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    mobileno = request.POST.get('mobileno')
    subject = 'regestration sucessfull of '+ str(name)
    body = 'your username '+ str(username) +'\nname '+ str(name) +'\nemail '+str(email) +'\nmobile no '+str(mobileno) +'\nif any error then please try again ' +'\nthank you ' +"\nNOTE don't reply to email "
    print(body)
    print(subject)
    send_mail(
    subject,
    body,
    'lifeevent2023@outlook.com',
    [
    email
    ],
    fail_silently=False)
    return redirect('ssuccess')

def slogin(request):
    return render(request,'speakerlogin/slogin.html')

def smultilogin(request):
    if (sUser.objects.filter(username=request.POST['username']).exists()):
        user = sUser.objects.filter(username=request.POST['username'])[0]

        request.session['id2'] = user.id
        request.session['usern'] = request.POST['username']
        return render(request,'speakerlogin/multilogin.html')
    return redirect('slogin')

def sgenmotp(request):

    a = request.session['usern']
    user = sUser.objects.get(username=a)
    mobile_no = user.mobileno
    otp = (random.randint(100000,999999))
    otpsms = 'Hey ' + str(a) + '\n' + ' The OTP for the login is ' + str(otp) + ' Please dont share with anybody' + ' \n send by life events '

    id = "TXTIND"
    # mobile_no = 9354317075
    senderid = "sender_id=" + id
    message = "&message=" + otpsms
    route = "&route=" + "v3"
    number = "&numbers=" + str(mobile_no)
    # payload = "sender_id=TXTIND&message=This is a test message&route=v3&numbers=9354317075"
    
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = senderid + message + route + number
    headers = {
      'authorization': "kaGNdrFqnTuZQ0hINefJ7IWn1UL4VX9u9l6u4AkbK8t1gQLzEa7aCSkJ6uVh",
      'Content-Type': "application/x-www-form-urlencoded",
      'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


    request.session['potp'] = otp
    return redirect('sotp')

def sotp(request):
    return render(request,'speakerlogin/loginmotp.html')

def sveriotp(request):
    a = request.POST.get('otp')
    b = request.session['potp']
    print(a)
    print(b)
    if str(a) == str(b):
        user = request.session['id2']
        del request.session['id2']
        del request.session['potp']
        request.session['id'] = user
        return redirect('ssuccess')
    return redirect('sotp')


def spassword(request):
    return render(request,'speakerlogin/loginpass.html')

def sverilogin(request):
    a = request.session['usern']
    print(a)
    del request.session['id2']
    if (sUser.objects.filter(username=a).exists()):
        user = sUser.objects.filter(username=request.session['usern'])[0]
        # request.session['id1'] = user.id
        if (request.POST.get('password')== user.password):
            request.session['id'] = user.id
            return redirect('ssuccess')
    return redirect('slogin')

def sgeneotp(request):
    a = request.session['usern']
    user = sUser.objects.get(username=a)
    sessionemail = user.email
    otp = (random.randint(100000,999999))
    
    
    otpsms = 'hey \n' + a + '\n' + 'The OTP for the login is ' + str(otp) + ' Please dont share with anybody \n please dont reply to this e-mail'

    subject = 'the otp for ' + a + '  life event login'
    body = otpsms
    send_mail(
    subject,
    body,
    'lifeevent2023@outlook.com',
    [
    sessionemail
    ],
    fail_silently=False)
    
    request.session['potp'] = otp
    return redirect('seotp')

def seotp(request):
    return render(request,'speakerlogin/logineotp.html')

def sverieotp(request):
    a = request.POST.get('otp')
    b = request.session['potp']
    print(a)
    print(b)
    if str(a) == str(b):
        user = request.session['id2']
        del request.session['id2']
        del request.session['potp']
        request.session['id'] = user
        return redirect('ssuccess')
    return redirect('seotp')

def ssuccess(request):
    user = sUser.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'speakerlogin/temp/about.html', context)

def sdsuccess(request):
    user = sUser.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'speakerlogin/sdetails.html', context)

def sabout(request):
    return render(request,'speakerlogin/temp/about.html')

def scontact(request):
    return render(request,'speakerlogin/temp/contact.html')

def sfaq(request):
    return render(request,'speakerlogin/temp/faq.html')

def sblog(request):
	context= {
	"blogs" : blogdetail.objects.all(),
	"comments" : comments.objects.all(),
	}
	return render(request,'speakerlogin/temp/blog.html',context)

def sreply(request):
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
	tanmay = requsearchcityest.FILES['image']
	user = comments.objects.create(name=request.POST['name'], content=request.POST['comment'], image=tanmay, date=now)
	user.save()
	return redirect('blog')
	context= {
	"blogs" : blogdetail.objects.all(),
	"comments" : comments.objects.all(),
	}
	return render(request,'speakerlogin/temp/blog.html',context)

def ssearchcity(request):
    return render(request,'speakerlogin/temp/search.html')

def ssearchpro(request):
    selectcity = request.POST.get('selectcity')
    if (search.objects.filter(city=selectcity).exists()):
        user = search.objects.filter(city=selectcity)[0]
        request.session['id'] = user.id
        return redirect('ssearchresult')
    return redirect('searchcity')

def ssearchresult(request):
    userr = search.objects.get(id=request.session['id'])
    context = {
        "userr": userr
    }
    return render(request, 'speakerlogin/temp/searchresult.html', context)

def sspeaker(request):

    context= {
	"userr" : sUser.objects.all(),
	}
    return render(request,'speakerlogin/temp/speakers-grid.html',context)

def slogout(request):
    del request.session['id']
    return redirect('page1')
