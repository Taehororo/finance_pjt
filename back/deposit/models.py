from django.db import models


class DepositProductsBaseInfo(models.Model):
    base_product_id = models.BigAutoField(primary_key=True, verbose_name="기본 상품 ID")
    fin_co_no = models.CharField(max_length=8, null=True, blank=True, verbose_name="금융회사 코드")
    kor_co_nm = models.CharField(max_length=255, null=True, blank=True, verbose_name="금융회사 명")
    fin_prdt_cd = models.CharField(max_length=15, null=True, blank=True, verbose_name="금융상품 코드")
    fin_prdt_nm = models.CharField(max_length=255, null=True, blank=True, verbose_name="금융 상품명")
    join_way = models.CharField(max_length=255, null=True, blank=True, verbose_name="가입 방법")
    mtrt_int = models.TextField(null=True, blank=True, verbose_name="만기 후 이자율")
    spcl_cnd = models.TextField(null=True, blank=True, verbose_name="우대조건")
    join_deny = models.CharField(max_length=1, null=True, blank=True, verbose_name="가입제한")
    join_member = models.CharField(max_length=255, null=True, blank=True, verbose_name="가입대상")
    etc_note = models.CharField(max_length=255, null=True, blank=True, verbose_name="기타 유의사항")
    max_limit = models.BigIntegerField(null=True, blank=True, verbose_name="최고한도")
    dcls_strt_day = models.CharField(max_length=8, null=True, blank=True, verbose_name="공시 시작일")
    dcls_end_day = models.CharField(max_length=8, null=True, blank=True, verbose_name="공시 종료일")
    fin_co_subm_day = models.CharField(max_length=14, null=True, blank=True, verbose_name="금융회사 제출일")

    class Meta:
        db_table = 'DepositProductsBaseInfo'
        verbose_name = "예금 상품 기본 정보"

    
class DepositProductsOption(models.Model):
    base_product = models.ForeignKey(DepositProductsBaseInfo, on_delete=models.CASCADE, related_name='options', verbose_name="기본 상품")
    fin_co_no = models.CharField(max_length=8, null=True, blank=True, verbose_name="금융회사 코드")
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True, verbose_name="금융상품 코드")
    intr_rate_type = models.CharField(max_length=1, null=True, blank=True, verbose_name="저축 금리 유형")
    intr_rate_type_nm = models.CharField(max_length=10, null=True, blank=True, verbose_name="저축 금리 유형명")
    save_trm = models.CharField(max_length=2, null=True, blank=True, verbose_name="저축 기간")
    intr_rate = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2, verbose_name="저축 금리")
    intr_rate2 = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2, verbose_name="최고 우대금리")

    class Meta:
        db_table = 'DepositProductsOption'
        verbose_name = "예금 상품 옵션"
        unique_together = ('fin_co_no', 'fin_prdt_cd', 'intr_rate_type', 'save_trm')