from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.posts.models import Post, PostComment, PostImages, PostLike
from apps.posts.serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostLikeSerializer, PostCommentSerializer, PostImagesSerializer
from apps.posts.permissions import PostPermissions

# Create your views here.
class PostAPIViewSet(GenericViewSet, ListModelMixin, 
                        RetrieveModelMixin, CreateModelMixin, 
                        UpdateModelMixin, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action in ("retrieve", "update", "partial_update",):
            return PostDetailSerializer
        elif self.action in ('create'):
            return PostCreateSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), PostPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class LikeAPIViewSet(GenericViewSet, ListModelMixin,
                        CreateModelMixin, DestroyModelMixin):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = (PostPermissions, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class CommentAPIViewSet(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = (PostPermissions, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class PostImagesAPIViewSet(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = PostImages.objects.all()
    serializer_class = PostImagesSerializer