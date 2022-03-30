from rest_framework import serializers
from .models import Users

## USER AUTH
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 

## OLD USERS DATABASE ##
class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ('id', 'user_name', 'password', 'high_score')
## ^^OLD USERS DATABASE^^ ##

## USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

## REGISTER SERIALIZER
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(
      validated_data['username'],
      validated_data['email'],
      validated_data['password'],
    )

    return User

## LOGIN SERIALIZER
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data) ## Bringing in authenticate from above via django
    if user and user.is_active: ## This is include with django auth by default
      return user
    raise serializers.ValidationError("Incorrect Credentials")



