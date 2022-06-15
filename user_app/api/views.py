from json import JSONEncoder
from rest_framework import serializers, views, generics, status
from django.contrib.auth.models import User
from user_app.api.serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app import models
from user_app.api import responses
from rest_framework_simplejwt import views as jwt_views

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

    def perform_create(self, serializer):
        user_created = serializer.save()
        password=serializer.validated_data["password"]
        user_created.set_password(password)

# @api_view(["POST"])
# def logout(request):
#     if request.method=="POST":
#         request.user.auth_token.delete()
#     return Response(data=responses.deleted(204,"Logout Successful !"),status=status.HTTP_204_NO_CONTENT)

class MyTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(["POST"])
def logout(request):
    print(request.user)
    return Response(status=status.HTTP_200_OK)