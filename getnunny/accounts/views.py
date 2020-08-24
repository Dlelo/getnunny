from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def home(request):
    orders = Order.objects.all()
    homeOwner = HouseOwner.objects.all()

    total_customers = homeOwner.count()
    total_orders = orders.count()
    delivered = orders.filter(status= 'Allocated').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders':orders, 'homeOwner':homeOwner, 'total_orders':total_orders}

    return render(request, 'accounts/dashboard.html', context)

def nunnys(request):
    nunnys = Nunny.objects.all()
    return render(request, 'accounts/nunnys.html', {'nunnys':nunnys})

def homeowner(request):
    return render(request, 'accounts/homeowner.html')
