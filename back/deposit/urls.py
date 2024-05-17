from django.urls import path
from . import views

app_name = 'deposit'
urlpatterns = [
    path('get/product/', views.get_deposit_products),
    path('products/', views.product_list)
]