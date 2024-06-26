# API 명세서
 
![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen)
![](https://img.shields.io/static/v1?label=&message=POST&color=yellow)
![](https://img.shields.io/static/v1?label=&message=PUT&color=blue)
![](https://img.shields.io/static/v1?label=&message=DELETE&color=red)
![](https://img.shields.io/static/v1?label=&message=EMIT&color=brightgreen)
![](https://img.shields.io/static/v1?label=&message=ON&color=blue) 
 
### 전체, 특정 상품 조회
<hr>

 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> (DB에 저장된) 전체 예금상품 목록조회 <br>
> http://127.0.0.1:8000/deposit/products/
 

 > ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> (DB에 저장된) 특정 예금상품 목록조회 <br>
> http://127.0.0.1:8000/deposit/products/ <br>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **content** | 18개월 |
> | **bankname** | 신한은행 |

 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> (DB에 저장된) 전체 정기적금상품 목록조회 <br>
> http://127.0.0.1:8000/saving/fixed/products/

 
 > ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> (DB에 저장된) 특정 정기적금상품 목록조회 <br>
> http://127.0.0.1:8000/saving/fixed/products/ <br>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **content** | 6개월 |
> | **bankname** | 하나은행 |

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

### 환율계산
<hr>

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

### 회원가입, 로그인, 프로필조회
<hr>

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

### 찜하기 기능
<hr>

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

<br>

### 각 상품들 찜한 여부 조회
<hr>

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

### 게시판 CRUD
<hr>

> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 게시글 목록 조회<br>
> **/articles/articles/**
>

> ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 게시글 생성 <br> 
> **/articles/articles/**
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰값 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **title** | 게시글 제목입니다 |
> | **content** | 게시글 내용입니다 |

<br>

> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 게시글 상세 조회<br>
> **/articles/articles/{id}/**
>


>![](https://img.shields.io/static/v1?label=&message=PUT&color=blue)<br>
> 게시글 전체필드 수정<br>
> **/articles/articles/{id}/**
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰값 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **title** | 게시글 제목 수정 |
> | **content** | 게시글 내용 수정 |

>![](https://img.shields.io/static/v1?label=&message=PATCH&color=purple)<br>
> 게시글 일부분 필드 수정<br>
> **/articles/articles/{id}/**
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰값 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **content** | 게시글 내용만 수정 |

>![](https://img.shields.io/static/v1?label=&message=DELETE&color=red)<br>
> 게시글 삭제<br>
> **/articles/articles/2/**
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰값 |  

<br>

### 댓글 CRUD
<hr>

> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 댓글 목록 조회<br>
> */articles/comments/*

> ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> 댓글 생성 <br>
> */articles/comments/*
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰값 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **article** | 1 |
> | **content** | 새로운 댓글입니다 |

<br>

> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 댓글 상세 조회<br>
> */articles/comments/{id}/*


>![](https://img.shields.io/static/v1?label=&message=PUT&color=blue)<br>
> 댓글 전체필드 수정<br>
> */articles/comments/{id}/*
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰값 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **article** | 1 |
> | **content** | 댓글 내용 수정합니다 |

>![](https://img.shields.io/static/v1?label=&message=PATCH&color=purple)<br>
> 댓글 일부분 필드 수정<br>
> */articles/comments/{id}/*
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰값 |  
>
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **article** | 1 |
> | **content** | 댓글 내용 수정합니다 |

>![](https://img.shields.io/static/v1?label=&message=DELETE&color=red)<br>
> 댓글 삭제<br>
> */articles/comments/{id}/*
> | **Request Header**  |  |
> | --- | --- |
> | **Authorization** | Token 토큰값 |  
>

<br>

### 챗봇에 질문하기
<hr>

> ![](https://img.shields.io/static/v1?label=&message=POST&color=yellow) <br>
> gpt에 질문 <br>
> **/recommender/chatbot/**
> | **Body** &nbsp; <sub>form-data</sub>  |  |
> | --- | --- |
> | **message** | 하나은행 상품을 추천해주세요 |
> | **productype** | freesaving |