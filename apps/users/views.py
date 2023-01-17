from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from apps.users.models import User 
from apps.users.serializers import UserSerializer, UserRegisterSerializer, UserDetailSerializer

# Create your views here.
class UsersAPIViewSet(GenericViewSet, ListModelMixin, 
                        RetrieveModelMixin, CreateModelMixin, 
                        UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ("retrieve", "update", "partial_update",):
            return UserDetailSerializer
        if self.action in ('create'):
            return UserRegisterSerializer
        return UserSerializer