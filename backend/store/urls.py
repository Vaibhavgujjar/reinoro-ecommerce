from django.urls import path
from .views import get_products, create_order, save_order,home

urlpatterns = [
    path('products/', get_products),
    path('payment/', create_order),
    path('save-order/', save_order),
    path('', home),
]