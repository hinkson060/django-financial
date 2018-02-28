from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('stock/<int:stock_id>/', views.stock_detail, name='stock_detail'),
    path('cryptocurrency/<int:crypto_id>/', views.crypto_detail, name='crypto_detail')
]