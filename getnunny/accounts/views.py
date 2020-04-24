from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def nunnys(request):
    return render(request, 'accounts/nunnys.html')

def homeowner(request):
    return render(request, 'accounts/homeowner.html')
