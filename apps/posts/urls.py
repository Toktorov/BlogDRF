from django.urls import path 
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet, LikeAPIViewSet

router = DefaultRouter()
router.register(prefix='post', viewset=PostAPIViewSet)
router.register(prefix='like', viewset=LikeAPIViewSet)

urlpatterns = router.urls