# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. Receieves the request and generates an HTTP page response

def index(request):
    return HttpResponse("<h1>This is the temp upload webpage</h1>")

def detail(request, upload_id):
    return HttpResponse("<h2>Details for upload id: " + str(upload_id) + "</h2>")