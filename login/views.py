from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,Register
from speakerlogin.models import sUser
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
def main(request):
    return render(request,'login/logregister.html')
def userregister(request):
    if (User.objects.filter(username=request.POST['username']).exists()):
        return redirect('main')
    if (request.POST.get('password')!=request.POST.get('repassword')):
        return redirect('main')
    user = User.objects.create(name=request.POST['name'], username=request.POST['username'], password=request.POST['password'], mobileno=request.POST['mobileno'],gender=request.POST['gender'],country=request.POST['country'],zipcode=request.POST['zipcode'],city=request.POST['city'],age=request.POST['age'],email=request.POST['email'])
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



    request.session['id1'] = user.id
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
    return redirect('success')

def login(request):
    return render(request,'login/login.html')

def multilogin(request):
    if (User.objects.filter(username=request.POST['username']).exists()):
        user = User.objects.filter(username=request.POST['username'])[0]

        request.session['id2'] = user.id
        request.session['usern'] = request.POST['username']
        return render(request,'login/multilogin.html')
    return redirect('login')

def genmotp(request):

    a = request.session['usern']
    user = User.objects.get(username=a)
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
    return redirect('otp')

def otp(request):
    return render(request,'login/loginmotp.html')

def veriotp(request):
    a = request.POST.get('otp')
    b = request.session['potp']
    print(a)
    print(b)
    if str(a) == str(b):
        user = request.session['id2']
        del request.session['id2']
        del request.session['potp']
        request.session['id1'] = user
        return redirect('success')
    return redirect('otp')


def password(request):
    return render(request,'login/loginpass.html')

def verilogin(request):
    a = request.session['usern']
    print(a)
    del request.session['id2']
    if (User.objects.filter(username=a).exists()):
        user = User.objects.filter(username=request.session['usern'])[0]
        request.session['id1'] = user.id
        if (request.POST.get('password')== user.password):
            request.session['id1'] = user.id
            return redirect('success')
    return redirect('login')

def geneotp(request):
    a = request.session['usern']
    user = User.objects.get(username=a)
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
    '''
    import http.client
    conn = http.client.HTTPSConnection("api.msg91.com")
    payload = str(final)
    headers = {
    'authkey': "292703ACVZuRCc7v5d70d3f9",
    'content-type': "application/json"
        }
    conn.request("POST", "/api/v2/sendsms", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    '''
    request.session['potp'] = otp
    return redirect('eotp')

def eotp(request):
    return render(request,'login/logineotp.html')

def verieotp(request):
    a = request.POST.get('otp')
    b = request.session['potp']
    print(a)
    print(b)
    if str(a) == str(b):
        user = request.session['id2']
        del request.session['id2']
        del request.session['potp']
        request.session['id1'] = user
        return redirect('success')
    return redirect('eotp')

def success(request):
    user = User.objects.get(id=request.session['id1'])
    context = {
        "user": user
    }
    return render(request, 'login/temp/about.html', context)

def dsuccess(request):
    user = User.objects.get(id=request.session['id1'])
    context = {
        "user": user
    }
    return render(request, 'login/details.html', context)

def mail(request):
    data = Register()
    data.name = request.POST.get('name')
    data.email = request.POST.get('email')
    data.mobileno = request.POST.get('mobileno')
    data.gender = request.POST.get('gender')
    data.occupation = request.POST.get('occupation')
    data.state = request.POST.get('state')
    data.age = request.POST.get('age')
    data.save()

    otpsms = 'Hey ' + str(data.name) + '\n' +  ' your registration is sucessfull ' + ' \nlife events '

    id = "TXTIND"
    # mobile_no = 
    senderid = "sender_id=" + id
    message = "&message=" + otpsms
    route = "&route=" + "v3"
    number = "&numbers=" + str(data.mobileno)
    # payload = "sender_id=TXTIND&message=This is a test message&route=v3&numbers=9354317075"
    
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = senderid + message + route + number
    headers = {
      'authorization': "kaGNdrFqnTuZQ0hINefJ7IWn1UL4VX9u9l6u4AkbK8t1gQLzEa7aCSkJ6uVh",
      'Content-Type': "application/x-www-form-urlencoded",
      'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    imf = 'imformation'
    name = request.POST.get('name')
    email = request.POST.get('email')
    mobileno = request.POST.get('mobileno')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    occupation = request.POST.get('occupation')
    state = request.POST.get('state')
    subject = 'regestration sucessfull of '+ str(name)
    body = 'your ' + str(imf) +'\nname '+ str(name) +'\nmobileno '+str(mobileno) +'\ngender '+str(gender) +'\nage '+str(age) +'\noccupation '+str(occupation) +'\nstate '+str(state) +'\nif any error then please try again ' +'\nthank you ' +"\nNOTE don't reply to email "
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
    return render(request,'login/temp/registersucess.html')
   

def logout(request):
    del request.session['id1']
    return redirect('page1')

def uabout(request):
    return render(request,'login/temp/about.html')

def ucontact(request):
    return render(request,'login/temp/contact.html')

def ufaq(request):
    return render(request,'login/temp/faq.html')

def ublog(request):
	context= {
	"blogs" : blogdetail.objects.all(),
	"comments" : comments.objects.all(),
	}
	return render(request,'login/temp/blog.html',context)

def ureply(request):
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
	return render(request,'login/temp/blog.html',context)

def usearchcity(request):
    return render(request,'login/temp/search.html')

def usearchpro(request):
    selectcity = request.POST.get('selectcity')
    if (search.objects.filter(city=selectcity).exists()):
        user = search.objects.filter(city=selectcity)[0]
        request.session['id'] = user.id
        return redirect('ssearchresult')
    return redirect('searchcity')

def usearchresult(request):
    userr = search.objects.get(id=request.session['id'])
    context = {
        "userr": userr
    }
    return render(request, 'login/temp/searchresult.html', context)

def uspeaker(request):

    context= {
	"userr" : sUser.objects.all(),
	}
    return render(request,'login/temp/speakers-grid.html',context)

def register(request):
    return render(request,'login/temp/registermail.html')
