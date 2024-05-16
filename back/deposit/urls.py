from django.urls import path
from . import views

app_name = 'deposit'
urlpatterns = [
    path('', views.get_deposit_products, name='index'),
]
