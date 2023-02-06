from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('suserregister',views.suserregister,name='suserregister'),
    path('smain',views.smain,name='smain'),
    path('ssuccess',views.ssuccess,name='ssuccess'),
    path('slogin',views.slogin,name='slogin'),
    path('smultilogin',views.smultilogin,name='smultilogin'),
    path('sgenmotp',views.sgenmotp,name='sgenmotp'),
    path('sotp',views.sotp,name='sotp'),
    path('sveriotp',views.sveriotp,name='sveriotp'),
    path('sgeneotp',views.sgeneotp,name='sgeneotp'),
    path('seotp',views.seotp,name='seotp'),
    path('sverieotp',views.sverieotp,name='sverieotp'),
    path('spassword',views.spassword,name='spassword'),
    path('sverilogin',views.sverilogin,name='sverilogin'),
    path('sdsuccess',views.sdsuccess,name='sdsuccess'),
    path('sabout',views.sabout,name='sabout'),
    path('scontact',views.scontact,name='scontact'),
    path('sfaq',views.sfaq,name='sfaq'),
    path('sblog',views.sblog,name='sblog'),
    path('sreply',views.sreply,name='sreply'),
    path('ssearchcity',views.ssearchcity,name='ssearchcity'),
    path('ssearchpro',views.ssearchpro,name='ssearchpro'),
    path('ssearchresult',views.ssearchresult,name='ssearchresult'),
    path('sspeaker',views.sspeaker,name='sspeaker'),
    path('slogout',views.slogout,name='slogout'),
    
    #path('comfirm',views.)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
