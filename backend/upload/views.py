# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. Receieves the request and generates an HTTP page response

def index(request):
    return HttpResponse("<h1>This is the temp upload webpage</h1>")