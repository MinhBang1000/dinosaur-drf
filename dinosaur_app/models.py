from pyexpat import model
from unicodedata import category
from django.db import models
from django.forms import ImageField, IntegerField

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Mesozoic(models.Model):
    name = models.CharField(max_length=50)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    desire = models.TextField(null=True)

    def __str__(self):
        return self.name

class Diet(models.Model):
    name = models.CharField(max_length=50)
    desire = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Dinosaur(models.Model):
    name = models.CharField(max_length=50)
    spell = models.CharField(max_length=50)
    explain = models.CharField(max_length=50)
    desire = models.TextField(null=True)
    author = models.TextField(null=True)
    length = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="dinosaurs")
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, related_name="dinosaurs")
    mesozoic = models.ManyToManyField(Mesozoic, related_name="dinosaurs")
    country = models.ManyToManyField(Country, related_name="dinosaurs")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(null=True)
    dinosaur = models.ForeignKey(Dinosaur, on_delete=models.CASCADE, related_name="image")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)
