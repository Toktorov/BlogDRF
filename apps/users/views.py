from rest_framework.generics import ListAPIView, CreateAPIView

from apps.users.models import User 
from apps.users.serializers import UserSerializer, UserRegisterSerializer

# Create your views here.
class UsersAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer