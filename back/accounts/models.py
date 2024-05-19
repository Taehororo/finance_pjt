from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100, default='')
    postcode = models.CharField(max_length=20, default='') 
    road_address = models.CharField(max_length=255, default='')
    jibun_address = models.CharField(max_length=255, default='')
    detail_address = models.CharField(max_length=255, default='')