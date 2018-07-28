from django.conf.urls import url
from . import views


urlpatterns = [
    # /upload/
    url(r'^$', views.index, name= 'index'), #current app name is $, it is the index page since there no extenstions to the /upload
    #go to views and go to a function called index to run the function
    # /upload/38947168...
    url(r'^(?P<upload_id>[0-9]+)/$' , views.detail, name='detail'),
]