from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.models import User, UserFollower
from apps.users.serializers import UserSerializer, UserRegisterSerializer, UserDetailSerializer, UserFollowerSerializer
from apps.users.permissions import UsersPermissions

# Create your views here.
class UsersAPIViewSet(GenericViewSet, ListModelMixin, 
                        RetrieveModelMixin, CreateModelMixin, 
                        UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        if self.action in ('create', ):
            return UserRegisterSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

class UserFollowerAPIView(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = UserFollower.objects.all()
    serializer_class = UserFollowerSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)