from rest_framework import viewsets,status
from rest_framework import permissions
from rest_framework.response import Response
from dinosaur_app.api import responses,viewsets as customizeviews
from django.contrib.auth.models import User
from dinosaur_app.models import Dinosaur, Category, Mesozoic, Diet, Country, Image
from dinosaur_app.api import serializers
from dinosaur_app.api import permissions as customizepermissions
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import FileSystemStorage
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from django.template.loader import render_to_string

class CategoryViewSet(customizeviews.BaseDinosaurViewSet):
    queryset=Category.objects.all()
    permission_classes=[permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return serializers.CategoryReadSerializer
        return serializers.CategoryWriteSerializer

class MesozoicViewSet(customizeviews.BaseDinosaurViewSet):
    queryset=Mesozoic.objects.all()
    serializer_class=serializers.MesozoicReadSerializer
    permission_classes=[customizepermissions.IsAdminToChange]

    def get_serializer_class(self):
        if self.action in ["list","retrieve"]:
            return serializers.MesozoicReadSerializer
        return serializers.MesozoicWriteSerializer

class DietViewSet(customizeviews.BaseDinosaurViewSet):
    queryset=Diet.objects.all()
    serializer_class=serializers.DietReadSerializer
    permission_classes=[customizepermissions.IsAdminToChange]
    
    def get_serializer_class(self):
        if self.action in ["list","retrieve"]:
            return serializers.DietReadSerializer
        return serializers.DietWriteSerializer

class CountryViewSet(customizeviews.BaseDinosaurViewSet):
    queryset=Country.objects.all()
    serializer_class=serializers.CountryReadSerializer
    permission_classes=[customizepermissions.IsAdminToChange]

    def get_serializer_class(self):
        if self.action in ["list","retrieve"]:
            return serializers.CountryReadSerializer
        return serializers.CountryWriteSerializer

class DinosaurViewSet(customizeviews.BaseDinosaurViewSet):
    queryset=Dinosaur.objects.all()
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    parser_classes=[MultiPartParser]

    # Filter
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields = "__all__"

    # Search
    # filter_backends=[filters.SearchFilter]
    # search_fields=[
    #     "name","length"
    # ]

    # Ordering
    # filter_backends=[filters.OrderingFilter]
    # ordering_fields='__all__'

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.DinosaurReadSerializer
        return serializers.DinosaurWriteSerializer

    def perform_create(self, serializer):
        dinosaur_created = serializer.save()
        images = self.request.data.getlist("image")
        fs = FileSystemStorage()
        for image in images:
            image_name =str(dinosaur_created.id)+"-"+image.name
            fs.save(image_name, image)
            url = fs.url(image_name)
            Image.objects.create(image=url, dinosaur=dinosaur_created)

    def perform_update(self, serializer):
        dinosaur_updated = serializer.save()
        images = self.request.data.getlist("image")
        fs = FileSystemStorage()
        for image in images:
            image_name = str(dinosaur_updated.id)+"-"+image.name
            file_exists = Image.objects.filter(image="/media/"+image_name)
            if not file_exists: # Check xem có ảnh này chưa
                fs.save(image_name, image)
                url = fs.url(image_name)
                Image.objects.create(image=url, dinosaur=dinosaur_updated)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        files = Image.objects.filter(dinosaur=instance)
        fs = FileSystemStorage()
        for file in files:
            file_name = str(file.image)[7:]
            fs.delete(file_name) # Chỉ lấy từ cái tên của file mà thôi
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(customizeviews.BaseDinosaurViewSet):
    queryset=User.objects.all()
    permission_classes=[permissions.IsAdminUser]
    serializer_class=serializers.UserSerializer

# Dinosaur Detail Via Mail For Person
@api_view(["GET"])
def mail(request, id):
    try:
        dinosaur = Dinosaur.objects.get(pk=id)
    except Dinosaur.DoesNotExist:
        return responses.error(code=404, message="Model with this key is not found!")
    subject="Information of "+dinosaur.name+". Detail Version"
    # message=f"- Name: {dinosaur.name}\n- Spell: {dinosaur.spell}\n- Explain: {dinosaur.explain}\n- Category: {dinosaur.category.name}"
    message = render_to_string("mail.html")
    email_from=settings.EMAIL_HOST_USER
    recipient_list = ["bradonleminhbang1@gmail.com", ]
    send_mail(subject, "Detail Page Of Dinosaur", email_from, recipient_list, html_message=message)
    return Response(data=responses.success(data=[],code=200,message="Send Mail Successful!"),status=status.HTTP_200_OK)
