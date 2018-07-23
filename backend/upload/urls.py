from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.index, name= 'index') #current app name is $, it is the index page since there no extenstions to the /upload
    #go to views and go to a function called index to run the function
]