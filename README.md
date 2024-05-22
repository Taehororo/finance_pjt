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


