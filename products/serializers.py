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

    username = serializers.ReadOnlyField(source = 'Profile.user')

    user = serializers.SlugRelatedField(
                    queryset = Profile.objects.all(),
                    slug_field = 'user_id'
                    )
                    
    product = serializers.SlugRelatedField(
                    queryset = product.objects.all(),
                    slug_field = 'title'
                    )


    class Meta:
        model = PurchaseRecord
        fields = ['username', 'user', 'product', 'quantity', 'Bought_on']


    def create(self, validated_data):
        print(validated_data)
        return PurchaseRecord.objects.create(**validated_data)


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