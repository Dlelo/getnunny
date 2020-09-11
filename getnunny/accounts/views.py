from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import OrderForm

def home(request):
    orders = Order.objects.all()
    homeOwner = HouseOwner.objects.all()
    nunnys = Nunny.objects.all()

    total_customers = homeOwner.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Allocated').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders':orders, 'homeOwner':homeOwner, 'total_orders':total_orders,'pending':pending,'delivered': delivered, "nunnys":nunnys}

    return render(request, 'accounts/dashboard.html', context)

def homeownerslist (request) :
    homeOwner = HouseOwner.objects.all()
    context = {'homeOwner':homeOwner}

    return render(request, 'accounts/homeowner.html', context)


def nunnys(request):
    nunnys = Nunny.objects.all()
    return render(request, 'accounts/nunnys.html', {'nunnys':nunnys})

def homeowner(request, pk_homeowner):
    homeowner = HouseOwner.objects.get(id=pk_homeowner)
    orders = homeowner.order_set.all()
    order_count = orders.count()

    context = {'homeowner': homeowner , 'orders':orders, 'order_count':order_count}
    return render(request, 'accounts/homeowners-detail-view.html', context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('printing POST', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk_order):
    order = Order.objects.get(id = pk_order)
    form = OrderForm(instance = order)

    if request.method == 'POST':
        # print('printing POST', request.POST)
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk_order):
    order = Order.objects.get(id = pk_order)
    
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)