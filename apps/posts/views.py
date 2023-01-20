from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.posts.models import Post, PostComment, PostImages, PostLike, PostFavotite
from apps.posts.serializers import PostSerializer, PostDetailSerializer, PostLikeSerializer, PostCommentSerializer, PostImagesSerializer, PostFavotiteSerializer
from apps.posts.permissions import PostPermissions

# Create your views here.
class PostAPIViewSet(GenericViewSet, ListModelMixin, 
                        RetrieveModelMixin, CreateModelMixin, 
                        UpdateModelMixin, DestroyModelMixin):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ('retrieve', 'update', 'partial_update',):
            return PostDetailSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action in ('list', 'update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), PostPermissions())
        return (AllowAny(), )

    def get_queryset(self):
        if self.action in ('list', ):
            return Post.objects.filter(user = self.request.user)
        return Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class LikeAPIViewSet(GenericViewSet, ListModelMixin,
                        CreateModelMixin, DestroyModelMixin):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class CommentAPIViewSet(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class PostImagesAPIViewSet(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = PostImages.objects.all()
    serializer_class = PostImagesSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        post = Post.objects.get(id = serializer.initial_data.get("post"))
        if serializer.is_valid() and post.user == request.user:
            serializer.save()
            return Response({"OK" : "Успешно создано"})
        return Response({"Error" : "Вы не можете добавить фотографию"})

class PostFavotiteAPIView(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = PostFavotite.objects.all()
    serializer_class = PostFavotiteSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)