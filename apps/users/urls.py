from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UsersAPIViewSet, UserFollowerAPIView

router = DefaultRouter()
router.register(prefix='users', viewset=UsersAPIViewSet)
router.register(prefix='follower', viewset=UserFollowerAPIView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]

urlpatterns += router.urls