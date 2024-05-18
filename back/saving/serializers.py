from rest_framework import serializers
from .models import SavingProductsBaseInfo, SavingProductsOption

class SavingProductsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProductsOption
        fields = '__all__'

class SavingProductsBaseInfoSerializer(serializers.ModelSerializer):
    options = SavingProductsOptionSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProductsBaseInfo
        fields = '__all__'