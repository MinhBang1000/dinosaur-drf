from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Diet)
admin.site.register(models.Mesozoic)
admin.site.register(models.Country)
admin.site.register(models.Dinosaur)
admin.site.register(models.Image)