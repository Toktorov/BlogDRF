from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from apps.posts.models import Post, PostComment, PostImages, PostLike
from apps.posts.serializers import PostSerializer, PostDetailSerializer

# Create your views here.
class PostAPIViewSet(GenericViewSet, ListModelMixin, 
                        RetrieveModelMixin, CreateModelMixin, 
                        UpdateModelMixin, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action in ("retrieve", "update", "partial_update",):
            return PostDetailSerializer
        return PostSerializer