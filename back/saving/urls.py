from django.urls import path
from . import views

app_name = 'saving'
urlpatterns = [
    path('get/product/', views.get_saving_products),
    path('products/', views.product_list),
]
