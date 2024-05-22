# 금융 프로젝트

## 프로젝트 역할
- 팀장: 전태호 (Front-End)
- 팀원: 오현진 (Back-End) 

## 설계 내용
### 메인 기능 
1. 예금 & 적금 금리비교 사이트
2. 환율변환
3. 근처은행
4. chatGPT를 이용한 상품 추천
5. 게시판

### 사용한 프레임워크
- <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=Vue.js&logoColor=white"/>
- <img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/>

### 사용한 기술
- Pinia (state관리 라이브러리)
- chart.js, vue-chartjs (vue에서 그래프출력)
- dj-rest-auth (django 로그인 회원가입관련 라이브러리)

### 사용한 API
- KaKaoMap API (근처은행검색에 사용)
- 다음카카오 우편번호 API (회원가입시 주소검색에 사용)
- 한국수출입은행 환율정보 API (환율변환에 사용)
- 금융감독원 API (예/적금 금리비교에 사용)
- chatGPT API (금융상품추천에 사용)


## [데이터베이스 모델링(ERD)](https://github.com/Taehororo/finance_pjt/blob/master/E-R%20diagram.md)


## ChatGPT API를 활용한 금융 상품 추천

1. 사용자는 원하는 금융 상품 종류(예금 or 정기적금 or 자유적금)를 선택하고 그 중 원하는 상품을 얻기위해 메시지를 입력함. 
<br>
(ex. 1년동안 1000만원을 가지고 저축할 상품을 추천해주세요.) 

2. 서버에서 사용자가 선택한 금융 상품 종류와 보낸 메시지를 전달받음
    ```python
    if request.method == 'POST':    
        try:
            data = request.data
            user_message = data.get('message', '')    # 사용자의 메시지
            product_type = data.get('producttype', '') # 사용자가 선택한 상품 유형
            if not user_message or not product_type:    # 메시지나 상품이 없다면
                return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST) # 에러상태 전송
    ``` 

3. 사용자가 선택한 금융상품 종류에 알맞는 데이터 배열 가져오기
   
    ```python
      # 사용자가 예금 상품을 원하면
      deposit_products_list = get_deposit_products()
    ```
4. '사용자가 입력한 메시지'와 '금융상품 종류에 알맞은 메시지' chatGPT 생성형 AI에게 전달
    ```python
      messages = [
          {'role': 'system', 'content': (
              "당신은 예금 상품 선택 도우미입니다."
              f"다음은 이용 가능한 예금상품 목록입니다: {deposit_products_list}"
              "사용자의 질문에 가장 적합한 상품을 추천해주세요."
              "메시지를 작성할 때 문장이 끊기지 않게 써주세요."
          )},
          {'role': 'user', 'content': user_message}
        ]

      data = {
          'model': 'gpt-3.5-turbo',
          'messages': messages,
          'max_tokens': 200,
          'stop': None
        }
      
      response = requests.post(url, headers=headers, json=data)
    ```

5. 생성형 AI에서는 답변을 생성
    ```python
      gpt_response = response.json()
      # choices 리스트의 첫 번째 요소에서 message 객체의 content 필드를 가져옴
      gpt_message = gpt_response['choices'][0]['message']['content']
      full_response += gpt_message
      
      if not gpt_response['choices'][0]['finish_reason'] == 'length':
          break
      messages.append({'role': 'assistant', 'content': gpt_message})
    ```

6. 생성형 AI가 최종적으로 만든 답변을 통해 특정 상품정보를 얻음
    ```python
      for product in products_list:
      if product['금융상품명'] in gpt_message:
          extract_product.append({
              'base_product_id': product['base_product_id'],
              'product_type': product_type,
          })
    ```

7. '생성형 AI의 답변'과 '특정 상품정보'를 클라이언트에게 보냄
    ```python
      return Response({"message": gpt_message, "product": product_data}, status=status.HTTP_200_OK)
    ```
8. 사용자는 AI의 답변을 보고 추천된 상품 정보를 확인할 수 있음. 추가적으로 추천된 상품 정보에 대한 상세 정보를 확인할 수 있음.
   
## 서비스 대표 기능들
### 1. 예/적금 금리비교

### 2. 환율변환
- 사용자는 입력 통화와 출력 통화를 선택하여 환율 계산을 즉시 가능

### 3. 근처은행

### 4. 상품 추천
- 사용자는 원하는 상품에 대해 자유롭게 질문할 수 있음
- AI 챗봇은 질문을 받고 상품 추천을 해줌
- 추가적으로 추천한 상품에 대해 상세정보 제공
- 사용자는 찜하기를 통해 해당 상품을 찜한 리스트에 저장 가능

### 5. 게시판



## 후기
- 데이터 활용 어려움
- 이상하게 잘 안됨