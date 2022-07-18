from rest_framework import serializers
from users.models import Profile

from .models import PurchaseRecord, category, manufacturer, product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = category
        fields = ['id', 'name', 'catDesc']


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = manufacturer
        fields = ['id', 'name', 'manDesc']


class PurchaseSerializer(serializers.ModelSerializer):

    username = serializers.SlugRelatedField(
                    queryset = Profile.objects.all(),
                    slug_field = 'username'
                    )
                    
    product = serializers.SlugRelatedField(
                    queryset = PurchaseRecord.objects.all(),
                    slug_field = 'title'
                    )


    class Meta:
        model = PurchaseRecord
        fields = ['username', 'product', 'quantity', 'Bought_on']


class ProductSerializer(serializers.ModelSerializer):

    cat = serializers.SlugRelatedField(
                    queryset = category.objects.all(),
                    slug_field = 'name'
                    )

    man = serializers.SlugRelatedField(
                    queryset = manufacturer.objects.all(),
                    slug_field = 'name'
                    )


    class Meta:
        model = product
        fields = ['id', 'title', 'proDesc', 'price', 'rating', 'cat', 'man']