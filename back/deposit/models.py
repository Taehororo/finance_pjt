from django.db import models
from django.conf import settings

class DepositProductsBaseInfo(models.Model):
    base_product_id = models.BigAutoField(primary_key=True)
    fin_co_no = models.CharField(max_length=8)
    kor_co_nm = models.CharField(max_length=255)
    fin_prdt_cd = models.CharField(max_length=15)
    fin_prdt_nm = models.CharField(max_length=255)
    join_way = models.CharField(max_length=255)
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.CharField(max_length=1)
    join_member = models.CharField(max_length=255)
    etc_note = models.CharField(max_length=255)
    max_limit = models.BigIntegerField(null=True, blank=True)
    dcls_strt_day = models.CharField(max_length=8, null=True, blank=True)
    dcls_end_day = models.CharField(max_length=8, null=True, blank=True)
    fin_co_subm_day = models.CharField(max_length=14, null=True, blank=True)

    class Meta:
        db_table = 'DepositProductsBaseInfo'

    
class DepositProductsOption(models.Model):
    base_product = models.ForeignKey(DepositProductsBaseInfo, on_delete=models.CASCADE, related_name='options')
    fin_co_no = models.CharField(max_length=8)
    fin_prdt_cd = models.CharField(max_length=20)
    intr_rate_type = models.CharField(max_length=1)
    intr_rate_type_nm = models.CharField(max_length=10)
    save_trm = models.CharField(max_length=2)
    intr_rate = models.DecimalField(max_digits=5, decimal_places=2)
    intr_rate2 = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'DepositProductsOption'
        unique_together = ('fin_co_no', 'fin_prdt_cd', 'intr_rate_type', 'intr_rate_type_nm', 'save_trm')