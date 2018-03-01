from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Customer, Stock, Crypto
from .forms import CustomerForm, StockForm, CryptoForm

from .models import Customer, Stock, Crypto

def index( request ):
    customers = Customer.objects.order_by('last_name')
    context = {
        'customers': customers,
    }
    return render( request, 'finances/index.html', context )

def customer_detail( request, customer_id ):
    customer = get_object_or_404( Customer, pk=customer_id )
    return render( request, 'finances/customer_detail.html', { 'customer': customer } )

def customer_create( request ):
    if request.method == 'POST':
        form = CustomerForm( request.POST )
        if form.is_valid():
            customer = form.save( commit = False )
            customer.save()
            return HttpResponseRedirect(reverse('customer_detail', args=(customer.id,)))
    else:
        form = CustomerForm()
    return render( request, 'finances/customer_create.html', {'form': form } )

def stock_detail( request, stock_id ):
    stock = get_object_or_404( Stock, pk=stock_id )
    return render( request, 'finances/stock_detail.html', { 'stock': stock } )
    
def stock_create( request, customer_id ):
    if request.method == 'POST':
        form = StockForm( request.POST )
        if form.is_valid():
            stock = form.save( commit = False )
            stock.owner = get_object_or_404( Customer, pk=customer_id )
            stock.save()
            return HttpResponseRedirect(reverse('stock_detail', args=(stock.id,)))
    else:
        form = StockForm()
        owner = customer_id
    return render( request, 'finances/stock_create.html', {'form': form, 'owner': owner } )

def crypto_detail( request, crypto_id ):
    crypto = get_object_or_404( Crypto, pk=crypto_id )
    return render( request, 'finances/crypto_detail.html', { 'crypto': crypto } )
    
def crypto_create( request, customer_id ):
    if request.method == 'POST':
        form = CryptoForm( request.POST )
        if form.is_valid():
            crypto = form.save( commit = False )
            crypto.owner = get_object_or_404( Customer, pk=customer_id )
            crypto.save()
            return HttpResponseRedirect(reverse('crypto_detail', args=(crypto.id,)))
    else:
        form = CryptoForm()
        owner = customer_id
    return render( request, 'finances/crypto_create.html', {'form': form, 'owner': owner } )
