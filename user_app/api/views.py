from urllib import response
from rest_framework import serializers, views, generics, status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from user_app.api.serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app import models
from user_app.api import responses
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt import tokens

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

    def perform_create(self, serializer):
        user_created = serializer.save()
        password=serializer.validated_data["password"]
        user_created.set_password(password)
        data = {
            "username": user_created.username,
            "password": password
        }
        self.user_created = authenticate(**data)

    # Use for JWT TOKEN CREATED
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        refresh = tokens.RefreshToken(self.user_created)
        data = response.data 
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        fotmatter = responses.success(data=data, code=201, message="Register Successful!")
        return Response(data=fotmatter, status=status.HTTP_201_CREATED)

# @api_view(["POST"])
# def logout(request):
#     if request.method=="POST":
#         request.user.auth_token.delete()
#     return Response(data=responses.deleted(204,"Logout Successful !"),status=status.HTTP_204_NO_CONTENT)

class MyTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        formatter = responses.success(data=response.data, code=200, message="Login Successful!")
        return Response(data=formatter, status=status.HTTP_200_OK)

@api_view(["POST"])
def logout(request):
    print(request.user)
    return Response(status=status.HTTP_200_OK)