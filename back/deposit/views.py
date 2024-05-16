from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import DepositProductsBaseInfo, DepositProductsOption
from django.http import HttpResponse 

# Create your views here.
def get_deposit_products(request):
    API_KEY = settings.API_KEY
    URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 정기예금 목록 저장
    response = requests.get(URL, params=params).json()
    baseList = response.get('result').get('baseList')  # 상품 목록 
    optionList = response.get('result').get('optionList') # 상품 옵션 목록

    # 데이터베이스에 저장
    for base_data in baseList:
        DepositProductsBaseInfo.objects.create(
            fin_co_no=base_data['fin_co_no'],
            fin_prdt_cd=base_data['fin_prdt_cd'],
            kor_co_nm=base_data['kor_co_nm'],
            fin_prdt_nm=base_data['fin_prdt_nm'],
            join_way=base_data['join_way'],
            mtrt_int=base_data['mtrt_int'],
            spcl_cnd=base_data['spcl_cnd'],
            join_deny=base_data['join_deny'],
            join_member=base_data['join_member'],
            etc_note=base_data['etc_note'],
            max_limit=base_data['max_limit'],
            dcls_strt_day=base_data['dcls_strt_day'],
            dcls_end_day=base_data['dcls_end_day'],
            fin_co_subm_day=base_data['fin_co_subm_day']
        )
    for option_data in optionList:
            base_instance = DepositProductsBaseInfo.objects.get(fin_prdt_cd=option_data['fin_prdt_cd'])
            DepositProductsOption.objects.create(
                base_product=base_instance,
                fin_co_no=option_data['fin_co_no'],
                fin_prdt_cd=option_data['fin_prdt_cd'],
                intr_rate_type=option_data['intr_rate_type'],
                intr_rate_type_nm=option_data['intr_rate_type_nm'],
                save_trm=option_data['save_trm'],
                intr_rate=option_data['intr_rate'],
                intr_rate2=option_data['intr_rate2']
            )
    return HttpResponse('Data saved to database') 
