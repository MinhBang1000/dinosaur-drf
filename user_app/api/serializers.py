from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError 
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from user_app.api import responses
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field=User.EMAIL_FIELD
    # Custom Serializer For Login By Email 
    def validate(self, attrs):
        password = attrs["password"]
        email = attrs["email"]
        try: 
            # Bằng email
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            # Bằng username
            # username = email
            raise ValidationError("Không chạy bằng username!")
        data = {
            "username": username,
            "password": password
        }
        try:
            data["request"] = self.context["request"]
        except KeyError:
            pass
        self.user = authenticate(**data)
        refresh = self.get_token(self.user)
        data = {
            "refresh": str(refresh),
            "access" : str(refresh.access_token)
        }
        return data

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=[
            "username",
            "password",
            "email"
        ]
        extra_kwargs={"password": {"write_only":True} }

    # Xài lại Token bình thường thì mở chỗ này ra
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data["token"] = Token.objects.get(user=instance).key
    #     return responses.created(data,201,"Register Successful !")
