from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UsersAPIView, UserRegisterAPIView


urlpatterns = [
    path('', UsersAPIView.as_view(), name = "api_users"),
    path('register/', UserRegisterAPIView.as_view(), name = "api_users_register"),
    #auth
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]