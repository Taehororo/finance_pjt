from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100, default='')
    postcode = models.CharField(max_length=20, default='') 
    roadaddress = models.CharField(max_length=255, default='')
    jibunaddress = models.CharField(max_length=255, default='')
    detailaddress = models.CharField(max_length=255, default='')