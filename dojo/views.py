# dojo/views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mysum(request, a, b=0, c=0 ):
    # request : HttpRequest
        return HttpResponse(int(a) + int(b) + int(c) + 100)