from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def home(request):
    orders = Order.objects.all()
    homeOwner = HouseOwner.objects.all()

    context = {'orders':orders, 'homeOwner':homeOwner}

    return render(request, 'accounts/dashboard.html', context)

def nunnys(request):
    nunnys = Nunny.objects.all()
    return render(request, 'accounts/nunnys.html', {'nunnys':nunnys})

def homeowner(request):
    return render(request, 'accounts/homeowner.html')
