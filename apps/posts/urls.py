from django.urls import path 
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=PostAPIViewSet
)

urlpatterns = router.urls