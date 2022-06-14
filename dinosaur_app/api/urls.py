from rest_framework.routers import DefaultRouter
from dinosaur_app.api import views
from django.urls import path, include

router = DefaultRouter()
router.register("dinosaur", views.DinosaurViewSet, basename="dinosaur")
router.register("user", views.UserViewSet, basename="user")
router.register("category", views.CategoryViewSet, basename="category")
router.register("mesozoic", views.MesozoicViewSet , basename="mesozoic")
router.register("diet", views.DietViewSet, basename="diet")
router.register("country", views.CountryViewSet, basename="country") 

urlpatterns = [
    path("", include(router.urls)),
    path("mail/<int:id>/", views.mail, name="mail"),
]
