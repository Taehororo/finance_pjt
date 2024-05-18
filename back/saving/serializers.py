from rest_framework import serializers
from .models import FixedSavingProductsBaseInfo, FixedSavingProductsOption, FreeSavingProductsBaseInfo, FreeSavingProductsOption

class FixedSavingProductsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedSavingProductsOption
        fields = '__all__'

class FixedSavingProductsBaseInfoSerializer(serializers.ModelSerializer):
    options = FixedSavingProductsOptionSerializer(many=True, read_only=True)

    class Meta:
        model = FixedSavingProductsBaseInfo
        fields = '__all__'

class FreeSavingProductsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSavingProductsOption
        fields = '__all__'

class FreeSavingProductsBaseInfoSerializer(serializers.ModelSerializer):
    options = FreeSavingProductsOptionSerializer(many=True, read_only=True)

    class Meta:
        model = FreeSavingProductsBaseInfo
        fields = '__all__'