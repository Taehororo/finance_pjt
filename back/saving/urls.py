from django.urls import path
from . import views

app_name = 'saving'
urlpatterns = [
    path('api/', views.get_saving_products),
    path('fixed/products/', views.fixed_product_list),
    path('free/products/', views.free_product_list),
]
