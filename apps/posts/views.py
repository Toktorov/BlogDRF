from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.posts.models import Post, PostComment, PostImages, PostLike
from apps.posts.serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer
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

    def get_queryset(self):
        return Post.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)