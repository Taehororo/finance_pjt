# 금융 프로젝트

## 프로젝트 역할
- 팀장: 전태호 (frontend - vue.js)
- 팀원: 오현진 (backend - django)

## 초기설정
### 기본설정
- 터미널 1
```
finance_pjt/

$ cd back
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements
```
- 터미널 2 
```
finance_pjt/

$ cd front
$ npm install
$ npm run dev
```

### 데이터베이스 초기설정 (필수사항)
### 선택 1. 저장되어있는 JSON 파일 데이터 로드 (2024-05-22 기준)
```
finance_pjt/back

$ python manage.py migrate
$ python manage.py loaddata fixtures/deposit_data.json
$ python manage.py loaddata fixtures/saving_data.json  
```
### 선택 2. 실시간 예적금 API 요청하여 데이터 로드
```
finance_pjt/back

$ python manage.py migrate
```
 
> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 예금 API 요청 후 DB에 저장 <br>
> http://127.0.0.1:8000/deposit/api
 
 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 적금 API 요청 후 DB에 저장 <br>
> http://127.0.0.1:8000/saving/api
>
> 
## 설계 내용
### 메인 기능 
1. 예금 & 적금 금리비교 사이트
2. 환율변환
3. 근처은행
4. chatGPT를 이용한 상품 추천
5. 게시판
### 사용한 기술
- Django
- Vue3
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


## 금융 상품 추천 


## 서비스 대표 기능들
### 1. 예/적금 금리비교

### 2. 환율변환

### 3. 근처은행

### 4. 상품 추천

### 5. 게시판



## 후기