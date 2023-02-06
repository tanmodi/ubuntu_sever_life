from django.urls import path
from . import views
urlpatterns = [
    path('searchcity',views.searchcity,name='searchcity'),
    path('searchpro',views.searchpro,name='searchpro'),
    path('searchresult',views.searchresult,name='searchresult'),
]
