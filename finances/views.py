from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

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

def stock_detail( request, stock_id ):
    stock = get_object_or_404( Stock, pk=stock_id )
    return render( request, 'finances/stock_detail.html', { 'stock': stock } )
 
def crypto_detail( request, crypto_id ):
    crypto = get_object_or_404( Crypto, pk=crypto_id )
    return render( request, 'finances/crypto_detail.html', { 'crypto': crypto } )
