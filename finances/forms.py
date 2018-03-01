from django import forms
from .models import Customer, Stock, Crypto

class CustomerForm( forms.ModelForm ):
    class Meta:
        model = Customer
        fields = (  'first_name', 'last_name', 'address_line_1',
                    'address_line_2', 'city', 'state', 'zipcode',
                    'email', 'phone' )

class StockForm( forms.ModelForm ):
    class Meta:
        model = Stock
        fields = ( 'symbol', 'name', 'purchase_price', 'purchase_date', 'quantity_owned' )

class CryptoForm( forms.ModelForm ):
    class Meta:
        model = Crypto
        fields = ( 'symbol', 'name', 'purchase_price', 'purchase_date', 'quantity_owned' )