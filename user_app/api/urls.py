from django.urls import path
from user_app.api.views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user_app.api import views

urlpatterns = [
    # path("register/", RegisterView.as_view(), name="register"),
    # path("login/", obtain_auth_token, name="login"),
    # path("logout/", views.logout, name="logout"),
    path('api/token/register/', views.RegisterView.as_view(), name="token_register"),
    path('api/token/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/remove/', views.logout, name="logout"),
]