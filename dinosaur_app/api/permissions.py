from rest_framework.permissions import BasePermission

class IsAdminToChange(BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if request.method in ["POST", "PUT", "DELETE"]:
            return user.is_superuser
        return super().has_permission(request, view) # True