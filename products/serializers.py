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

    username = serializers.SerializerMethodField()

    user = serializers.SlugRelatedField(
                    queryset = Profile.objects.all(),
                    slug_field = 'user_id'
                    )
                    
    product = serializers.SlugRelatedField(
                    queryset = product.objects.all(),
                    slug_field = 'title'
                    )

    price = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseRecord
        fields = ['user', 'username', 'product', 'quantity' ,'price', 'Bought_on']

    def get_price(self, obj):
        return obj.product.price * obj.quantity

    def get_username(self, obj):
        return obj.user.user.username
        

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