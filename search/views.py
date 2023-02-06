from django.shortcuts import render,redirect, HttpResponse
from .models import search
from django.contrib import messages
# Create your views here.

def searchcity(request):
    return render(request,'search/search.html')
def searchpro(request):
    selectcity = request.POST.get('selectcity')
    if (search.objects.filter(city=selectcity).exists()):
        user = search.objects.filter(city=selectcity)[0]
        request.session['id'] = user.id
        return redirect('searchresult')
    return redirect('searchcity')

def searchresult(request):
    user = search.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'search/searchresult.html', context)
