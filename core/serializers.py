from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()
    
ALL_FIELDS = '__all__'

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['password', 'email', 'full_name', 'phone_number', 'age']

class UserSerializer(BaseUserSerializer):
    email = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)

    class Meta(BaseUserSerializer.Meta):
        fields = ['email', 'full_name', 'phone_number', 'age', "uuid"]
