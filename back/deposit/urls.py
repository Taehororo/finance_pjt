from django.urls import path
from . import views

app_name = 'deposit'
urlpatterns = [
    path('api/', views.get_deposit_products),
    path('products/', views.product_list),
    path('like/<int:product_id>/', views.like_deposit_product),
    path('like/check/<int:product_id>/', views.check_like_deposit_product),
]
