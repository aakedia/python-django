from rest_framework import serializers
from .models import Category, Product, ProductVariations


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductVariationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariations
        fields = '__all__'
