from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=100)
    postcode = serializers.CharField(max_length=20)
    road_address = serializers.CharField(max_length=255)
    jibun_address = serializers.CharField(max_length=255)
    detail_address = serializers.CharField(max_length=255)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['name'] = self.validated_data.get('name', '')
        data['postcode'] = self.validated_data.get('postcode', '')
        data['road_address'] = self.validated_data.get('road_address', '')
        data['jibun_address'] = self.validated_data.get('jibun_address', '')
        data['detail_address'] = self.validated_data.get('detail_address', '')
        return data

    def save(self, request):
        user = super().save(request)
        user.name = self.cleaned_data.get('name')
        user.postcode = self.cleaned_data.get('postcode')
        user.road_address = self.cleaned_data.get('road_address')
        user.jibun_address = self.cleaned_data.get('jibun_address')
        user.detail_address = self.cleaned_data.get('detail_address')
        user.save()
        return user