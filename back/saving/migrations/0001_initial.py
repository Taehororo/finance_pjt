# Generated by Django 4.2.8 on 2024-05-18 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavingProductsBaseInfo',
            fields=[
                ('base_product_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='기본 상품 ID')),
                ('fin_co_no', models.CharField(max_length=20, verbose_name='금융회사 코드')),
                ('kor_co_nm', models.CharField(max_length=255, verbose_name='금융회사 명')),
                ('fin_prdt_cd', models.CharField(max_length=100, verbose_name='금융상품 코드')),
                ('fin_prdt_nm', models.CharField(max_length=255, verbose_name='금융 상품명')),
                ('join_way', models.CharField(max_length=255, verbose_name='가입 방법')),
                ('mtrt_int', models.TextField(verbose_name='만기 후 이자율')),
                ('spcl_cnd', models.TextField(verbose_name='우대조건')),
                ('join_deny', models.CharField(max_length=5, verbose_name='가입제한')),
                ('join_member', models.CharField(max_length=255, verbose_name='가입대상')),
                ('etc_note', models.CharField(max_length=255, verbose_name='기타 유의사항')),
                ('max_limit', models.BigIntegerField(blank=True, null=True, verbose_name='최고한도')),
                ('dcls_strt_day', models.CharField(blank=True, max_length=8, null=True, verbose_name='공시 시작일')),
                ('dcls_end_day', models.CharField(blank=True, max_length=8, null=True, verbose_name='공시 종료일')),
                ('fin_co_subm_day', models.CharField(blank=True, max_length=14, null=True, verbose_name='금융회사 제출일')),
            ],
            options={
                'db_table': 'SavingProductsBaseInfo',
            },
        ),
        migrations.CreateModel(
            name='SavingProductsOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.CharField(max_length=20, verbose_name='금융회사 코드')),
                ('fin_prdt_cd', models.CharField(max_length=50, verbose_name='금융상품 코드')),
                ('intr_rate_type', models.CharField(max_length=10, verbose_name='저축 금리 유형')),
                ('intr_rate_type_nm', models.CharField(max_length=30, verbose_name='저축 금리 유형명')),
                ('rsrv_type', models.CharField(max_length=1, verbose_name='적립 유형')),
                ('rsrv_type_nm', models.CharField(max_length=30, verbose_name='적립 유형명')),
                ('save_trm', models.CharField(max_length=2, verbose_name='저축 기간')),
                ('intr_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='저축 금리')),
                ('intr_rate2', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='최고 우대금리')),
                ('base_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='saving.savingproductsbaseinfo', verbose_name='기본 상품')),
            ],
            options={
                'db_table': 'SavingProductsOption',
                'unique_together': {('fin_co_no', 'fin_prdt_cd', 'intr_rate_type', 'rsrv_type', 'save_trm')},
            },
        ),
    ]
