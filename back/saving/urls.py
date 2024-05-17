from django.urls import path
from . import views

app_name = 'saving'
urlpatterns = [
    path('', views.index, name='index'),
]
