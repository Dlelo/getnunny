from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home')

def nunnys(request):
    return HttpResponse('nunnys')

def homeowner(request):
    return HttpResponse('homeowner')
