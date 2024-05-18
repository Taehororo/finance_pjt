from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
import requests
from .models import FixedSavingProductsBaseInfo, FixedSavingProductsOption, FreeSavingProductsBaseInfo, FreeSavingProductsOption
from .serializers import FixedSavingProductsBaseInfoSerializer, FixedSavingProductsOptionSerializer, FreeSavingProductsBaseInfoSerializer, FreeSavingProductsOptionSerializer
from django.http import HttpResponse 
import pprint
import re


# Django와 외부 API를 통해 데이터를 가져와서 데이터베이스에 저장하는 뷰
def get_saving_products(request):
    # API 키와 URL을 설정
    API_KEY = settings.API_KEY
    URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 적금 목록 저장
    response = requests.get(URL, params=params).json()
    baseList = response.get('result').get('baseList')  # 상품 목록 
    optionList = response.get('result').get('optionList') # 상품 옵션 목록

    # 각 baseList 항목을 사전으로 변환하여 빠른 검색 가능하게 함
    base_dict = {item['fin_prdt_cd']: item for item in baseList}

    # 옵션 데이터를 순회하며 기본 데이터를 저장하고, 옵션 데이터를 연결
    for option_data in optionList:
        fin_prdt_cd = option_data['fin_prdt_cd']
        base_data = base_dict.get(fin_prdt_cd)

        if not base_data:
            continue

        if option_data['rsrv_type'] == 'S':  # 정기적금
            base_instance, created = FixedSavingProductsBaseInfo.objects.update_or_create(
                fin_prdt_cd=base_data['fin_prdt_cd'],
                defaults={
                    'fin_co_no': base_data['fin_co_no'],
                    'kor_co_nm': base_data['kor_co_nm'],
                    'fin_prdt_nm': base_data['fin_prdt_nm'],
                    'join_way': base_data['join_way'],
                    'mtrt_int': base_data['mtrt_int'],
                    'spcl_cnd': base_data['spcl_cnd'],
                    'join_deny': base_data['join_deny'],
                    'join_member': base_data['join_member'],
                    'etc_note': base_data['etc_note'],
                    'max_limit': base_data['max_limit'],
                    'dcls_strt_day': base_data['dcls_strt_day'],
                    'dcls_end_day': base_data['dcls_end_day'],
                    'fin_co_subm_day': base_data['fin_co_subm_day']
                }
            )
            FixedSavingProductsOption.objects.update_or_create(
                base_product=base_instance,
                fin_co_no=option_data['fin_co_no'],
                fin_prdt_cd=option_data['fin_prdt_cd'],
                intr_rate_type=option_data['intr_rate_type'],
                save_trm=option_data['save_trm'],
                defaults={
                    'intr_rate_type_nm': option_data['intr_rate_type_nm'],
                    'intr_rate': option_data['intr_rate'],
                    'intr_rate2': option_data['intr_rate2']
                }
            )
        elif option_data['rsrv_type'] == 'F':  # 자유적금
            base_instance, created = FreeSavingProductsBaseInfo.objects.update_or_create(
                fin_prdt_cd=base_data['fin_prdt_cd'],
                defaults={
                    'fin_co_no': base_data['fin_co_no'],
                    'kor_co_nm': base_data['kor_co_nm'],
                    'fin_prdt_nm': base_data['fin_prdt_nm'],
                    'join_way': base_data['join_way'],
                    'mtrt_int': base_data['mtrt_int'],
                    'spcl_cnd': base_data['spcl_cnd'],
                    'join_deny': base_data['join_deny'],
                    'join_member': base_data['join_member'],
                    'etc_note': base_data['etc_note'],
                    'max_limit': base_data['max_limit'],
                    'dcls_strt_day': base_data['dcls_strt_day'],
                    'dcls_end_day': base_data['dcls_end_day'],
                    'fin_co_subm_day': base_data['fin_co_subm_day']
                }
            )
            FreeSavingProductsOption.objects.update_or_create(
                base_product=base_instance,
                fin_co_no=option_data['fin_co_no'],
                fin_prdt_cd=option_data['fin_prdt_cd'],
                intr_rate_type=option_data['intr_rate_type'],
                save_trm=option_data['save_trm'],
                defaults={
                    'intr_rate_type_nm': option_data['intr_rate_type_nm'],
                    'intr_rate': option_data['intr_rate'],
                    'intr_rate2': option_data['intr_rate2']
                }
            )

    return HttpResponse('Data saved to database')


@api_view(['GET','POST'])
def fixed_product_list(request):
    # 모든 정기적금 상품 목록을 12개월 기준 최고우대금리 내림차순 정렬로 반환
    if request.method == 'GET':
        save_term = '12'    # 기본저축기간 12개월
        bank_name = '전체은행'      # 전체은행
    
    # 상품 목록을 특정 저축기간 최고우대금리 내림차순 정렬로 반환
    elif request.method =='POST':
        save_term = request.data.get('content', '') # vue로부터 전달받은 저축기간 (ex: 6개월)
        save_term = re.findall(r'\d+', save_term)   # 저축기간 숫자 리스트형태로 추출 (ex: ['6'])
        save_term = save_term[0] if save_term else '0'  # 저축기간 숫자 추출 (ex: 6)
        bank_name = request.data.get('bankname', '')    # vue로부터 전달받은 은행이름

    # 데이터베이스에서 정기적금 상품 필터링 (은행 필터링 포함)
    if bank_name != '전체은행':
        products = FixedSavingProductsBaseInfo.objects.filter(kor_co_nm=bank_name)
    elif bank_name == '전체은행':
        # 데이터베이스에서 모든 정기적금 상품을 가져옴
        products = FixedSavingProductsBaseInfo.objects.all()
        
        
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
        except FixedSavingProductsOption.DoesNotExist:
            # 선택된 저축기간 option이 없는 상품인 경우
            product_with_highest_rates.append({
            'product': product,
            'highest_option_rate': float('-inf'),  # 정렬을 위한 처리
            'has_rate': False
            })
    
    # 저축기간 기준 최고금리 내림차순 정렬
    sorted_products = sorted(product_with_highest_rates, key=lambda x: (x['has_rate'], x['highest_option_rate']), reverse=True)

    # sorted products 정렬된 목록 
    sorted_products_only = [x['product'] for x in sorted_products]

    # Serialize and return the sorted products
    serializer = FixedSavingProductsBaseInfoSerializer(sorted_products_only, many=True)

    return Response(serializer.data)
    

@api_view(['GET','POST'])
def free_product_list(request):
    # 모든 자유적금 상품 목록을 12개월 기준 최고우대금리 내림차순 정렬로 반환
    if request.method == 'GET':
        save_term = '12'    # 기본저축기간 12개월
        bank_name = '전체은행'      # 전체은행
    
    # 상품 목록을 특정 저축기간 최고우대금리 내림차순 정렬로 반환
    elif request.method =='POST':
        save_term = request.data.get('content', '') # vue로부터 전달받은 저축기간 (ex: 6개월)
        save_term = re.findall(r'\d+', save_term)   # 저축기간 숫자 리스트형태로 추출 (ex: ['6'])
        save_term = save_term[0] if save_term else '0'  # 저축기간 숫자 추출 (ex: 6)
        bank_name = request.data.get('bankname', '')    # vue로부터 전달받은 은행이름

    # 데이터베이스에서 자유적금 상품 필터링 (은행 필터링 포함)
    if bank_name != '전체은행':
        products = FreeSavingProductsBaseInfo.objects.filter(kor_co_nm=bank_name)
    elif bank_name == '전체은행':
        # 데이터베이스에서 모든 자유적금 상품을 가져옴
        products = FreeSavingProductsBaseInfo.objects.all()
    

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
        except FreeSavingProductsOption.DoesNotExist:
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
    serializer = FreeSavingProductsBaseInfoSerializer(sorted_products_only, many=True)
    # pprint.pprint(serializer.data)

    return Response(serializer.data)