from django.db import models

class Customer( models.Model ):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50 )
    address_line_1 = models.CharField( max_length = 50 )
    address_line_2 = models.CharField( max_length = 50 )
    city = models.CharField( max_length = 50 )
    state = models.CharField( max_length = 2 )
    zipcode = models.CharField( max_length = 6 )
    email = models.CharField( max_length = 254 )
    phone = models.CharField( max_length = 10 )
    

class Stock( models.Model ):
    stock_owner = models.ForeignKey( Customer, on_delete = models.CASCADE )
    stock_symbol = models.CharField( max_length = 5 )
    stock_name = models.CharField( max_length = 50 )
    stock_purchase_price = models.DecimalField( max_digits = 6, decimal_places = 2 )
    stock_purchase_date = models.DateField()
    stock_quantity_owned = models.IntegerField()
    
class Crypto( models.Model ):
    crypto_owner = models.ForeignKey( Customer, on_delete = models.CASCADE )
    crypto_symbol = models.CharField( max_length = 5 )
    crypto_name = models.CharField( max_length = 50 )
    purchase_price = models.DecimalField( max_digits = 6, decimal_places = 2 )
    purchase_date = models.DateField()
    quantity_owned = models.IntegerField()