# API 명세서
 
![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen)
![](https://img.shields.io/static/v1?label=&message=POST&color=yellow)
![](https://img.shields.io/static/v1?label=&message=PUT&color=blue)
![](https://img.shields.io/static/v1?label=&message=DELETE&color=red)
![](https://img.shields.io/static/v1?label=&message=EMIT&color=brightgreen)
![](https://img.shields.io/static/v1?label=&message=ON&color=blue) 
 
### API Description
 
> ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 예금 api 불러와서 DB에 저장 <br>
> http://127.0.0.1:8000/deposit/api
 
 > ![](https://img.shields.io/static/v1?label=&message=GET&color=darkgreen) <br>
> 적금 api 불러와서 DB에 저장 <br>
> http://127.0.0.1:8000/saving/api

<br>
<hr>
<br>

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
<br>

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