from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
import requests
from django.http import HttpResponse 
import pprint
from datetime import datetime, timedelta

# 글로벌 변수로 환율 데이터를 저장
EXCHANGE_DATA = None
EXCHANGE_DATE = None
# API 키와 URL을 설정
API_KEY = settings.EXCHANGE_API_KEY
URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

def fetch_exchange_rates(search_date):
    # 날짜를 'YYYYMMDD' 형식으로 변환
    search_date_str = search_date.strftime('%Y%m%d')
    params = {
        'authkey': API_KEY,
        'searchdate': search_date_str,
        'data': 'AP01'
    }

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        exchange_data = response.json()
        if exchange_data:  # 데이터가 비어 있지 않으면 반환
            return exchange_data, search_date_str
        else:  # 데이터가 비어 있으면 전날 데이터를 가져옴
            previous_date = search_date - timedelta(days=1)
            return fetch_exchange_rates(previous_date)
    else:
        return None, None
    

# 가장 가까운 날의 데이터를 fetch하고, 미국달러와 한국원의 일주일간의 데이터 return
@api_view(['GET'])
def get_exchange_rates(request):
    global EXCHANGE_DATA, EXCHANGE_DATE

    today = datetime.today()
    exchange_data, exchange_date = fetch_exchange_rates(today)
    if exchange_data is None:
        return Response({'error': 'Failed to fetch exchange rates'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    EXCHANGE_DATA = exchange_data
    EXCHANGE_DATE = exchange_date

    first_country_dates, first_country_rates, second_country_dates, second_country_rates = fetch_dates_and_rates_for_period('미국 달러', '한국 원')

    return Response({'input_country': {'dates': first_country_dates, 'rates': first_country_rates}, 'output_country': {'dates': second_country_dates, 'rates': second_country_rates}}, status=status.HTTP_200_OK)


# 두개 국가의 일주일 간 dates과 rates 배열을 반환 하는 함수
def fetch_dates_and_rates_for_period(first_country, second_country):
    # 오늘 날짜 설정
    today = datetime.today()
    dates = [(today - timedelta(days=i)).strftime('%Y%m%d') for i in range(10)] 

    # 데이터를 저장할 리스트 초기화
    first_country_data = []
    second_country_data = []

    for date in dates:
        if len(first_country_data) == 7 and len(second_country_data) == 7:
            break

        url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate={date}&data=AP01'
        response = requests.get(url)
        data = response.json()
        if not data:
            continue
        
        # USD 데이터 추출
        for item in data:
            if item['cur_nm'] == first_country:
                rate = float(item['kftc_deal_bas_r'].replace(',', ''))
                first_country_data.append((date, rate))
            
            elif item['cur_nm'] == second_country:
                rate = float(item['kftc_deal_bas_r'].replace(',', ''))
                second_country_data.append((date, rate))

        # 날짜 기준으로 정렬
        first_country_data.sort(key=lambda x: x[0])
        second_country_data.sort(key=lambda x: x[0])

        first_country_dates, first_country_rates = zip(*first_country_data)
        second_country_dates, second_country_rates = zip(*second_country_data)

    return first_country_dates, first_country_rates, second_country_dates, second_country_rates


@api_view(['POST'])
def calculate_exchange(request):
    global EXCHANGE_DATA, EXCHANGE_DATE
    if request.method == 'POST':
        try:
            data = request.data
            input_country = data.get('inputcountry')
            output_country = data.get('outputcountry')
            amount = float(data.get('money'))
            
            # 특정국가의 날짜 배열과 환율 배열 
            first_country_dates, first_country_rates, second_country_dates, second_country_rates = fetch_dates_and_rates_for_period(input_country, output_country)

            # 환율계산파트
            if EXCHANGE_DATA is None:
                return Response({'error': 'Exchange rates not available'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            # available_currencies = [item["cur_nm"] for item in exchange_data]   # 환율 데이터의 모든 cur_nm 값 출력

            # 입력통화 및 출력통화에 해당하는 환율 찾기
            input_rate = next((item for item in EXCHANGE_DATA if item["cur_nm"].strip() == input_country.strip()), None)
            output_rate = next((item for item in EXCHANGE_DATA if item["cur_nm"].strip() == output_country.strip()), None)

            if input_rate and output_rate:
                input_rate_value = float(input_rate['kftc_deal_bas_r'].replace(',', ''))
                output_rate_value = float(output_rate['kftc_deal_bas_r'].replace(',', ''))

                # JPY(100), IDR(100) 같은 경우를 처리
                if "(100)" in input_rate['cur_unit']:
                    input_rate_value /= 100
                if "(100)" in output_rate['cur_unit']:
                    output_rate_value /= 100

                result = (amount / output_rate_value) * input_rate_value     # 환율 계산
                result = round(result, 2)     # 결과를 소수점 아래 둘째 자리까지 반올림
                # 계산된 환율, 날짜 보내기
                return Response({'result': result, 'exchange_date': EXCHANGE_DATE, 'input_country': {'dates': first_country_dates, 'rates': first_country_rates}, 
                                'output_country': {'dates': second_country_dates, 'rates': second_country_rates}}, status=status.HTTP_200_OK) 
            else:
                return Response({'error': 'Invalid currency code'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)