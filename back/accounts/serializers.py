from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from deposit.serializers import DepositProductsBaseInfoSerializer
from saving.serializers import FixedSavingProductsBaseInfoSerializer, FreeSavingProductsBaseInfoSerializer

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=100)
    postcode = serializers.CharField(max_length=20)
    roadaddress = serializers.CharField(max_length=255)
    jibunaddress = serializers.CharField(max_length=255)
    detailaddress = serializers.CharField(max_length=255)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['name'] = self.validated_data.get('name', '')
        data['postcode'] = self.validated_data.get('postcode', '')
        data['roadaddress'] = self.validated_data.get('roadaddress', '')
        data['jibunaddress'] = self.validated_data.get('jibunaddress', '')
        data['detailaddress'] = self.validated_data.get('detailaddress', '')
        return data

    def save(self, request):
        user = super().save(request)
        user.name = self.cleaned_data.get('name')
        user.postcode = self.cleaned_data.get('postcode')
        user.roadaddress = self.cleaned_data.get('roadaddress')
        user.jibunaddress = self.cleaned_data.get('jibunaddress')
        user.detailaddress = self.cleaned_data.get('detailaddress')
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    liked_deposit_products = DepositProductsBaseInfoSerializer(many=True, read_only=True)
    liked_fixed_saving_products = FixedSavingProductsBaseInfoSerializer(many=True, read_only=True)
    liked_free_saving_products = FreeSavingProductsBaseInfoSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'postcode', 'roadaddress', 'jibunaddress', 'detailaddress', 'liked_deposit_products', 'liked_fixed_saving_products', 'liked_free_saving_products']