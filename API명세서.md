# API 명세서
 
![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen)
![](https://img.shields.io/static/v1?label=&message=POST&color=yellow)
![](https://img.shields.io/static/v1?label=&message=PUT&color=blue)
![](https://img.shields.io/static/v1?label=&message=DELETE&color=red)
![](https://img.shields.io/static/v1?label=&message=EMIT&color=brightgreen)
![](https://img.shields.io/static/v1?label=&message=ON&color=blue) 
 
## API Description
 
> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 예금 api 불러와서 DB에 저장 <br>
> http://127.0.0.1:8000/deposit/api
 
 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 적금 api 불러와서 DB에 저장 <br>
> http://127.0.0.1:8000/saving/api

<br>
<hr>

### 전체, 특정 상품 조회

 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> (DB에 저장된) 전체 예금상품 목록조회 <br>
> http://127.0.0.1:8000/deposit/products/
 

 > ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> (DB에 저장된) 특정 예금상품 목록조회 <br>
> http://127.0.0.1:8000/deposit/products/ <br>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **content** | 12개월 |
> | **bankname** | 전체은행 |

 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> (DB에 저장된) 전체 정기적금상품 목록조회 <br>
> http://127.0.0.1:8000/saving/fixed/products/

 
 > ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> (DB에 저장된) 특정 정기적금상품 목록조회 <br>
> http://127.0.0.1:8000/saving/fixed/products/ <br>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **content** | 12개월 |
> | **bankname** | 전체은행 |

 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> (DB에 저장된) 전체 자유적금상품 목록조회 <br>
> http://127.0.0.1:8000/saving/free/products/

 > ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> (DB에 저장된) 특정 자유적금상품 목록조회 <br>
> http://127.0.0.1:8000/saving/free/products/ <br>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **content** | 12개월 |
> | **bankname** | 전체은행 |

<br>
<hr>

### 환율계산

 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 환율계산 요청 불러오기 <br>
> http://127.0.0.1:8000/exchange/api


 > ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 환율계산 요청<br>
> http://127.0.0.1:8000/exchange/calculate/ <br>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **inputcountry** | 미국 달러 |
> | **outputcountry** | 한국 원 |
> | **money** | 10 |

<br>
<hr>

### 회원가입, 로그인, 프로필조회

 > ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 회원가입 요청<br>
> http://127.0.0.1:8000/accounts/signup/ <br>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **name** | 사람이름 |
> | **postcode** | 우편번호 |
> | **road_address** | 도로명 |
> | **jibun_address** | 지번주소 |
> | **detail_address** | 상세주소 |
> | **username** | 아이디 |
> | **email** | 이메일 |
> | **password1** | 비밀번호 |
> | **password2** | 비밀번호 확인 |

 > ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 로그인 요청<br>
> http://127.0.0.1:8000/accounts/login/ <br>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **username** | 아이디 |
> | **password** | 비밀번호 |
>
> | **Response**  |  |
> | --- | --- |
> {
>    "key": "토큰"
> }

> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 유저정보 조회 <br>
> http://127.0.0.1:8000/accounts/user/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  

<br>
<hr>

### 찜하기 기능
> ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 예금상품 찜하기 <br>
> http://127.0.0.1:8000/deposit/like/<<int:product_id>>/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
> 
> | **Response**  |  |
> | --- | --- |
> {
>    "message": "해당 예금 상품이 찜한 목록에 추가되었습니다.",
>    "liked": true
>  }

> ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 정기적금상품 찜하기 <br>
> http://127.0.0.1:8000/saving/like_fixed/<<int:product_id>>/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
> 
> | **Response**  |  |
> | --- | --- |
> {
>    "message": "해당 정기적금 상품이 찜한 목록에 추가되었습니다.",
>    "liked": true
>  }

> ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 자유적금상품 찜하기 <br>
> http://127.0.0.1:8000/saving/like_free/<<int:product_id>>/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
> 
> | **Response**  |  |
> | --- | --- |
> {
>    "message": "해당 자유적금 상품이 찜한 목록에 추가되었습니다.",
>    "liked": true
>  }
>
### 각 상품들 찜한 여부 조회
> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 예금상품 찜여부 조회 <br>
> http://127.0.0.1:8000/deposit/like/check/<<int:product_id>>/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
> 
> | **Response**  |  |
> | --- | --- |
> {
>    "liked": true
> }

> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 정기적금상품 찜여부 조회 <br>
> http://127.0.0.1:8000/saving/like_fixed/check/<<int:product_id>>/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
>
> | **Response**  |  |
> | --- | --- |
> {
>    "liked": true
>  }

> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 자유적금상품 찜여부 조회 <br>
> http://127.0.0.1:8000/saving/like_free/check/<<int:product_id>>/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
>
>  | **Response**  |  |
> | --- | --- |
> {
>    "liked": true
> }
>
<br>
<hr>

### 게시판 CRUD
> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 게시글 목록 조회<br>
> http://127.0.0.1:8000/articles/
>

> ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 게시글 생성 <br>
> http://127.0.0.1:8000/articles/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **title** | 게시글 제목입니다 |
> | **content** | 게시글 내용입니다 |

<br>
<hr>

> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 게시글 상세 조회<br>
> http://127.0.0.1:8000/articles/2/
>


>![](https://img.shields.io/static/v1?label=&message=PUT&color=blue)<br>
> 게시글 전체 수정<br>
> http://127.0.0.1:8000/articles/2/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **title** | 게시글 제목 수정 |
> | **content** | 게시글 내용 수정 |

>![](https://img.shields.io/static/v1?label=&message=PATCH&color=purple)<br>
> 게시글 부분 수정<br>
> http://127.0.0.1:8000/articles/2/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **content** | 게시글 내용만 수정 |

>![](https://img.shields.io/static/v1?label=&message=DELETE&color=red)<br>
> 게시글 삭제<br>
> http://127.0.0.1:8000/articles/2/
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰 |  