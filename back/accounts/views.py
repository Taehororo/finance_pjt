from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from django.http import JsonResponse
from rest_framework import status


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    # 디버깅
    # def post(self, request, *args, **kwargs):
    #     # 요청 데이터를 출력
    #     print(request.data)

    #     serializer = CustomRegisterSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(request)
    #         return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)