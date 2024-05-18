from django.urls import path
from . import views

app_name = 'exchange'
urlpatterns = [
    path('api/', views.get_exchange_rates),
]
