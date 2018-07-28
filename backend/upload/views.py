# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import FileUpload

# Create your views here. Receieves the request and generates an HTTP page response

def index(request):
    all_uploads = FileUpload.objects.all()
    html = ''
    for upload in all_uploads:
        url = '/upload/'+str(upload.id) + '/'
        html += ' <a href= "' + url + '"> ' + upload.filename + '</a><br>'
    return HttpResponse(html)

   

def detail(request, upload_id):
    return HttpResponse("<h2>Details for upload id: " + str(upload_id) + "</h2>")