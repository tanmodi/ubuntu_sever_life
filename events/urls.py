"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app.views import page4,page13,page6,page7,page8,page9,page11,page1,Contactus,newsletter

#from otp.views import pver,potp
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('index-2.html',page1,name='page1'),


    path('contact.html',page4,name='page4'),
    path('faq.html',page13,name='page13'),
    path('gallery.html',page6,name='page6'),
    path('',page7,name='page7'),
    path('about.html',page8,name='page8'),

    path('speakers-grid.html',page11,name='page11'),


    path('contactus',Contactus,name='Contactus'),
    path('newsletter',newsletter,name='newsletter'),
    path('', include('login.urls')),
    path('', include('search.urls')),
    path('',include('blog.urls')),
    path('',include('speakerlogin.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
