from dataclasses import field
from django.contrib.auth.models import User
from django.forms import ValidationError 
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from user_app.api import responses
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(data)
        return responses.success(data=data, code=200, message="Login Successful!")

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=[
            "username",
            "password",
            "email"
        ]
        extra_kwargs={"password": {"write_only":True} }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["token"] = Token.objects.get(user=instance).key
        return responses.created(data,201,"Register Successful !")