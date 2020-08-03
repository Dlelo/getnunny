from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def home(request):
    return render(request, 'accounts/dashboard.html')

def nunnys(request):
    nunnys = Nunny.objects.all()
    return render(request, 'accounts/nunnys.html', {'nunnys':nunnys})

def homeowner(request):
    return render(request, 'accounts/homeowner.html')
