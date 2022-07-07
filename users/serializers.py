from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = newUser
        fields = ['username', 'email', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source = "user.username")
    class Meta:
        model = Profile
        fields = ['id', 'address', 'joinedDate', 'user']
