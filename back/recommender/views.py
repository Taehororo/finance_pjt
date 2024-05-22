from django.conf import settings
from deposit.models import DepositProductsBaseInfo
from saving.models import FixedSavingProductsBaseInfo, FreeSavingProductsBaseInfo
from deposit.serializers import DepositProductsBaseInfoSerializer
from saving.serializers import FixedSavingProductsBaseInfoSerializer, FreeSavingProductsBaseInfoSerializer
import requests, json, pprint
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

'''
예금, 정기적금, 자유적금 상품정보 데이터베이스에서 가져오기
'''
def get_deposit_products():
    deposit_products = DepositProductsBaseInfo.objects.all()
    print(len(deposit_products))
    deposit_list = []
    for product in deposit_products:
        options = product.options.all()
        options_list = []
        for option in options:
            options_list.append({
                '저축 금리 유형명': option.intr_rate_type_nm,
                '저축 기간(개월)': option.save_trm,
                '저축 금리': option.intr_rate,
                '최고 우대금리': option.intr_rate2
            })
        deposit_list.append({
            '유형': '예금',
            'base_product_id': product.base_product_id,
            '은행명': product.kor_co_nm,
            '금융상품명': product.fin_prdt_nm,
            # '가입방법': product.join_way,
            # '만기율 이자율': product.mtrt_int,
            # '우대조건': product.spcl_cnd,
            # '가입대상': product.join_member,
            # '기타 유의사항': product.etc_note,
            '금리정보': options_list,
        })

    return deposit_list


def get_fixed_saving_products():
    fixed_saving_products = FixedSavingProductsBaseInfo.objects.all()
    fixed_saving_list = []
    for product in fixed_saving_products:
        options = product.options.all()
        options_list = []
        for option in options:
            options_list.append({
                '저축 금리 유형명': option.intr_rate_type_nm,
                '저축 기간(개월)': option.save_trm,
                '저축 금리': option.intr_rate,
                '최고 우대금리': option.intr_rate2,
            })
        fixed_saving_list.append({
            '유형': '정기적금',
            'base_product_id': product.base_product_id,
            '은행명': product.kor_co_nm,
            '금융상품명': product.fin_prdt_nm,
            # '가입방법': product.join_way,
            # '만기율 이자율': product.mtrt_int,
            # '우대조건': product.spcl_cnd,
            # '가입대상': product.join_member,
            # '기타 유의사항': product.etc_note,
            '금리정보': options_list,
        })

    return fixed_saving_list


def get_free_saving_products():
    free_saving_products = FreeSavingProductsBaseInfo.objects.all()
    free_saving_list = []
    for product in free_saving_products:
        options = product.options.all()
        options_list = []
        for option in options:
            options_list.append({
                '저축 금리 유형명': option.intr_rate_type_nm,
                '저축 기간(개월)': option.save_trm,
                '저축 금리': option.intr_rate,
                '최고 우대금리': option.intr_rate2,
            })
        free_saving_list.append({
            '유형': '자유적금',
            'base_product_id': product.base_product_id,
            '은행명': product.kor_co_nm,
            '금융상품명': product.fin_prdt_nm,
            # '가입방법': product.join_way,
            # '만기율 이자율': product.mtrt_int,
            # '우대조건': product.spcl_cnd,
            # '가입대상': product.join_member,
            # '기타 유의사항': product.etc_note,
            '금리정보': options_list,
        })

    return free_saving_list


'''
CHAT GPT API 사용해서 금융 추천 서비스 만들기
'''
def extract_product_id(gpt_message, product_type):
    if product_type == 'deposit':
        products_list = get_deposit_products()
    elif product_type == 'fixedsaving':
        products_list = get_fixed_saving_products()
    elif product_type == 'freesaving':
        products_list = get_free_saving_products()

    extract_product = []
    for product in products_list:
        if product['금융상품명'] in gpt_message:
            extract_product.append({
                'base_product_id': product['base_product_id'],
                'product_type': product_type,
            })
    return extract_product


# 상품 추천
def recommend_product(user_message, product_type):
    # 예금 상품 추천
    if product_type == 'deposit':
        deposit_products_list = get_deposit_products()
        messages = [
            {'role': 'system', 'content': (
                "당신은 예금 상품 선택 도우미입니다."
                f"다음은 이용 가능한 예금상품 목록입니다: {deposit_products_list}"
                "사용자의 질문에 가장 적합한 상품을 추천해주세요."
                "메시지를 작성할 때 문장이 끊기지 않게 써주세요."
            )},
            {'role': 'user', 'content': user_message}
        ]

    # 정기적금 상품 추천
    elif product_type == 'fixedsaving':
        fixed_saving_products_list = get_fixed_saving_products()
        messages = [
            {'role': 'system', 'content': (
                "당신은 정기적금 상품 선택 도우미입니다."
                f"다음은 이용 가능한 정기적금 상품 목록입니다: {fixed_saving_products_list}"
                "사용자의 질문에 가장 적합한 상품을 추천해주세요."
                "메시지를 작성할 때 문장이 끊기지 않게 써주세요."
            )},
            {'role': 'user', 'content': user_message}
        ]

    # 자유적금 상품 추천       
    elif product_type == 'freesaving':
        free_saving_products_list = get_free_saving_products()
        messages = [
            {'role': 'system', 'content': (
                "당신은 자유적금 상품 선택 도우미입니다."
                f"다음은 이용 가능한 자유적금상품 목록입니다: {free_saving_products_list}"
                "사용자의 질문에 가장 적합한 상품을 추천해주세요."
                "메시지를 작성할 때 문장이 끊기지 않게 써주세요."
            )},
            {'role': 'user', 'content': user_message}
        ]  
    
    full_response = ""
    API_KEY = settings.CHATGPT_API_KEY
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    while True:
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': messages,
            'max_tokens': 200,
            'stop': None
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code != 200:
            print(f"Error: API request failed with status code {response.status_code}")
            print(f"Response: {response.text}")
            return None, None
        
        try:
            gpt_response = response.json()
            gpt_message = gpt_response['choices'][0]['message']['content']
        except (KeyError, IndexError, TypeError) as e:
            print("Error: Unexpected API response format")
            print(f"Response: {response.text}")
            return None, None
        
        full_response += gpt_message
        
        if not gpt_response['choices'][0]['finish_reason'] == 'length':
            break
        
        messages.append({'role': 'assistant', 'content': gpt_message})
    
    return full_response, extract_product_id(full_response, product_type)


# 추천서비스 챗봇
@api_view(['POST'])
def chatbot(request):
    if request.method == 'POST':    
        try:
            data = request.data
            # 예시
            # user_message = "저는 1년동안 최대 이익을 얻고싶어요."
            # product_type = "fixedsaving"
            user_message = data.get('message', '')  # 사용자의 질문
            product_type = data.get('producttype', '') # 사용자가 선택한 상품 유형
            if not user_message or not product_type:    # 질문이나 상품이 없다면
                return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)
            
            gpt_message, extract_product = recommend_product(user_message, product_type)    # GPT에서 만들어준 답변, {상품아이디, 상품유형}을 추출
            if not gpt_message: # GPT에서 만들어준 답변이 없으면
                return Response({"error": "Failed to get a valid response from the API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # extract_product를 기반으로 실제 상품 정보를 가져와 시리얼라이저를 사용해 직렬화
            product_data = []
            for item in extract_product:
                if item['product_type'] == 'deposit':
                    product_instance = DepositProductsBaseInfo.objects.get(base_product_id=item['base_product_id'])
                    serializer = DepositProductsBaseInfoSerializer(product_instance)
                elif item['product_type'] == 'fixedsaving':
                    product_instance = FixedSavingProductsBaseInfo.objects.get(base_product_id=item['base_product_id'])
                    serializer = FixedSavingProductsBaseInfoSerializer(product_instance)
                elif item['product_type'] == 'freesaving':
                    product_instance = FreeSavingProductsBaseInfo.objects.get(base_product_id=item['base_product_id'])
                    serializer = FreeSavingProductsBaseInfoSerializer(product_instance)
                
                product_data.append(serializer.data)

            return Response({"message": gpt_message, "product": product_data}, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)




