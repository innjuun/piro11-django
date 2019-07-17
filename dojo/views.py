# dojo/views.py
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def mysum(request, numbers):
    # request : HttpRequest
    # numbers = "1/2/3/4/5/2/5/...
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)
