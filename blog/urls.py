from django.urls import path
from . import views
urlpatterns = [
    path('blog.html',views.blog,name='blog'),
    path('reply',views.reply,name='reply')
    ]
