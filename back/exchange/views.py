from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
import requests
from django.http import HttpResponse 
import pprint
import re


def get_exchange_rates(request):
    # API 키와 URL을 설정
    API_KEY = settings.EXCHANGE_API_KEY
    URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': API_KEY,
        'searchdate': '20240517',
        'data': 'AP01'
    }

    response = requests.get(URL, params=params).json()