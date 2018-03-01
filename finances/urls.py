from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customer_create/', views.customer_create, name='customer_create'),
    
    
    path('stock/<int:stock_id>/', views.stock_detail, name='stock_detail'),
    path('stock_create/<int:customer_id>', views.stock_create, name='stock_create'),
    
    path('cryptocurrency/<int:crypto_id>/', views.crypto_detail, name='crypto_detail'),
    path('crypto_create/<int:customer_id>', views.crypto_create, name='crypto_create')
]