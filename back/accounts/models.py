from django.db import models
from django.contrib.auth.models import AbstractUser
from deposit.models import DepositProductsBaseInfo
from saving.models import FixedSavingProductsBaseInfo, FreeSavingProductsBaseInfo

class User(AbstractUser):
    name = models.CharField(max_length=100, default='')
    postcode = models.CharField(max_length=20, default='') 
    roadaddress = models.CharField(max_length=255, default='')
    jibunaddress = models.CharField(max_length=255, default='')
    detailaddress = models.CharField(max_length=255, default='')
    liked_deposit_products = models.ManyToManyField(DepositProductsBaseInfo, related_name='liked_by_users', blank=True)
    liked_fixed_saving_products = models.ManyToManyField(FixedSavingProductsBaseInfo, related_name='liked_by_users_fixed', blank=True)
    liked_free_saving_products = models.ManyToManyField(FreeSavingProductsBaseInfo, related_name="liked_by_users_free", blank=True)