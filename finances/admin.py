from django.contrib import admin

from .models import Customer, Stock, Crypto

admin.site.register(Customer)
admin.site.register(Stock)
admin.site.register(Crypto)