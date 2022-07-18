from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.IntegerField()
    fullname = serializers.SerializerMethodField("get_User_fullname")

    class Meta:
        model = Profile
        fields = ['id', 'user','user_id', 'address','fullname', 'joined_date']

    def create(self, validated_data):
        print(validated_data)
        print(type(validated_data['user']))
        user = User.objects.get(id = validated_data['user']['id'])
        validated_data['user'] = user
        return Profile.objects.create(**validated_data)

    def get_User_fullname(self, obj):
        return obj.user.password + obj.user.username
