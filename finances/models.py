import datetime

from django.db import models
from django.utils import timezone

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
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Stock( models.Model ):
    owner = models.ForeignKey( Customer, on_delete = models.CASCADE )
    symbol = models.CharField( max_length = 5 )
    name = models.CharField( max_length = 50 )
    purchase_price = models.DecimalField( max_digits = 6, decimal_places = 2 )
    purchase_date = models.DateField()
    quantity_owned = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Crypto( models.Model ):
    owner = models.ForeignKey( Customer, on_delete = models.CASCADE )
    symbol = models.CharField( max_length = 5 )
    name = models.CharField( max_length = 50 )
    purchase_price = models.DecimalField( max_digits = 6, decimal_places = 2 )
    purchase_date = models.DateField()
    quantity_owned = models.IntegerField()
    
    def __str__(self):
        return self.name
