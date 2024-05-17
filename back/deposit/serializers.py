from rest_framework import serializers
from .models import DepositProductsBaseInfo, DepositProductsOption

class DepositProductsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProductsOption
        fields = '__all__'

class DepositProductsBaseInfoSerializer(serializers.ModelSerializer):
    options = DepositProductsOptionSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProductsBaseInfo
        fields = '__all__'