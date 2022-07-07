from rest_framework import serializers

from .models import category, manufacturer, product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id', 'name', 'catDesc']

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = manufacturer
        fields = ['id', 'name', 'manDesc']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source = "cat.name")
    manufacturer_name = serializers.CharField(source = "man.name")
    class Meta:
        model = product
        fields = ['id', 'title', 'proDesc', 'price', 'rating', 'category_name', 'manufacturer_name']
        depth = 1
