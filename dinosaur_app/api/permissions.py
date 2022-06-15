from rest_framework.permissions import IsAuthenticated ,BasePermission
from django.contrib.auth.models import User, Permission
class IsAdminToChange(BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if request.method in ["POST", "PUT", "DELETE"]:
            return user.is_superuser
        return super().has_permission(request, view) # True

class IsReadDinosaur(IsAuthenticated):

    def has_permission(self, request, view):
        user = request.user
        permissions = Permission.objects.filter(user=user, codename="view_dinosaur")
        if len(permissions) != 0:
            return super().has_permission(request, view)
        return False