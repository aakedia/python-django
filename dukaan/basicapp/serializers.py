from rest_framework import serializers
from .models import Category, Product, ProductVariations


# Serializer for category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# Serializer for Product Variations model
class ProductVariationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariations
        fields = '__all__'
