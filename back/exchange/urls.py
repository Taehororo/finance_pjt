from django.urls import path
from . import views

app_name = 'exchange'
urlpatterns = [
    # path('api/', views.get_exchange_rates),
    path('calculate/', views.calculate_exchange),
]
