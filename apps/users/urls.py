from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UsersAPIViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=UsersAPIViewSet
)

urlpatterns = [
    #auth
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]

urlpatterns += router.urls