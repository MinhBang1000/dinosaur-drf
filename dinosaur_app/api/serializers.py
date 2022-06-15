from pyexpat import model
from django.forms import ValidationError
from rest_framework import serializers,status
from dinosaur_app.models import Dinosaur, Category, Mesozoic, Diet, Country
from dinosaur_app.api import responses
from rest_framework.response import Response
from django.contrib.auth.models import User

# Category
class CategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        depth=2

class CategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

# Mesozoic
class MesozoicReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mesozoic
        fields="__all__"

class MesozoicWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mesozoic
        fields="__all__"

# Diet
class DietReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Diet
        fields="__all__"
        depth=2

class DietWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Diet
        fields="__all__"

# Country
class CountryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields="__all__"
        depth=2

class CountryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields="__all__"

# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        depth=2
        extra_kwargs = {'password': {'write_only': True}}

# Dinosaur
class DinosaurWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dinosaur
        fields="__all__"

    def validate(self, attrs):            
        # fields = [
        #     "name", 
        #     "spell",
        #     "explain",
        #     "desire",
        #     "author",
        #     "length", 
        #     "weight",
        #     "category",
        #     "diet", 
        #     "mesozoic",
        #     "country"
        # ]
        # if Dinosaur.objects.filter(name=attrs["name"]).exists():
        #     raise ValidationError({
        #         "name" : "A dinosaur name have already exists !"
        #     })
        return super().validate(attrs)


class DinosaurReadSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(read_only=True, many=True)
    category = serializers.StringRelatedField(read_only=True)
    diet = serializers.StringRelatedField(read_only=True)
    mesozoic = serializers.StringRelatedField(read_only=True, many=True)
    image = serializers.StringRelatedField(many=True)
    class Meta:
        model=Dinosaur
        fields="__all__"

