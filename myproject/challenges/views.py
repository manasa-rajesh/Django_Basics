from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Welcomw to January")

def february(request):
    return HttpResponse('Welcome to February')
