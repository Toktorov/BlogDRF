from django.urls import path 
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet, LikeAPIViewSet, CommentAPIViewSet, PostImagesAPIViewSet

router = DefaultRouter()
router.register(prefix='post', viewset=PostAPIViewSet)
router.register(prefix='like', viewset=LikeAPIViewSet)
router.register(prefix='comment', viewset=CommentAPIViewSet)
router.register(prefix='post_images', viewset=PostImagesAPIViewSet)

urlpatterns = router.urls