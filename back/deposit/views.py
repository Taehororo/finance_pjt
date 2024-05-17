from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
import requests
from .models import DepositProductsBaseInfo, DepositProductsOption
from .serializers import DepositProductsBaseInfoSerializer, DepositProductsOptionSerializer
from django.http import HttpResponse 
import pprint
import re


# Django와 외부 API를 통해 데이터를 가져와서 데이터베이스에 저장하는 뷰
def get_deposit_products(request):
    # API 키와 URL을 설정
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



@api_view(['GET','POST'])
def product_list(request):
    # 모든 예금 상품 목록을 12개월 기준 최고우대금리 내림차순 정렬로 반환
    if request.method == 'GET':
        # 첫 화면 정렬 기준은 12개월
        save_term = '12'
    
    # 상품 목록을 특정 저축기간 최고우대금리 내림차순 정렬로 반환
    elif request.method =='POST':
        # vue로 부터 전달받은 저축기간 (ex: 6개월)
        save_term = request.data.get('content', '')
        # 저축기간 숫자 리스트형태로 추출 (ex: ['6'])
        save_term = re.findall(r'\d+', save_term)
        # 저축기간 숫자 추출 (ex: 6)
        save_term = save_term[0] if save_term else '0'

    # 데이터베이스에서 모든 예금 상품을 가져옴
    products = get_list_or_404(DepositProductsBaseInfo)
        

    product_with_highest_rates = []
    for product in products:
        try:
            # 선택된 저축기간에 따른 option 조회
            option = product.options.get(save_trm=save_term)
            product_with_highest_rates.append({
            'product': product,
            'highest_option_rate': option.intr_rate2,
            'has_rate': True
            })
        except DepositProductsOption.DoesNotExist:
            # 선택된 저축기간 option이 없는 상품인 경우
            product_with_highest_rates.append({
            'product': product,
            'highest_option_rate': float('-inf'),  # 정렬을 위한 처리
            'has_rate': False
            })
    
    # 저축기간 기준 최고금리 내림차순 정렬
    sorted_products = sorted(product_with_highest_rates, key=lambda x: (x['has_rate'], x['highest_option_rate']), reverse=True)
    # pprint.pprint(sorted_products)

    # sorted products 정렬된 목록 
    sorted_products_only = [x['product'] for x in sorted_products]
    # pprint.pprint(sorted_products_only)

    # Serialize and return the sorted products
    serializer = DepositProductsBaseInfoSerializer(sorted_products_only, many=True)
    # pprint.pprint(serializer.data)

    return Response(serializer.data)
    
