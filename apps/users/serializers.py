from rest_framework import serializers

from apps.users.models import User, UserFollower
from apps.posts.serializers import PostSerializer, PostFavotiteSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'phone_number', 'profile_image')

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length = 255, write_only=True
    )
    email = serializers.CharField(
        max_length = 255, write_only=True
    )
    phone_number = serializers.CharField(
        max_length = 255, write_only=True
    )
    age = serializers.IntegerField(
        write_only=True
    )
    password = serializers.CharField(
        max_length = 255, write_only=True
    )
    password2 = serializers.CharField(
        max_length = 255, write_only=True
    )

    class Meta:
        model = User 
        fields = ('username', 'email', 'phone_number', 'age', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({"phone_number": "Напишите номер с +996"})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password2')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollower
        fields = "__all__"

class UserDetailSerializer(serializers.ModelSerializer):
    #posts - посты пользователя
    user_posts = PostSerializer(read_only = True, many = True)
    count_posts = serializers.SerializerMethodField(read_only = True)
    #subscribers - подписчики
    subscribers = UserFollowerSerializer(read_only = True, many = True)
    count_subscribers = serializers.SerializerMethodField(read_only = True)
    #subscriptions - подписки
    subscriptions = UserFollowerSerializer(read_only = True, many = True)
    count_subscriptions = serializers.SerializerMethodField(read_only = True)
    #favorites - избранные пользователя
    favorites = PostFavotiteSerializer(read_only = True, many = True)
    count_favorites = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
            'last_name', 'email', 'date_joined', 
            'phone_number', 'profile_image', 'user_posts', 
            'count_posts', 'subscribers', 'count_subscribers', 
            'subscriptions', 'count_subscriptions', 'favorites', 'count_favorites'
        )

    def get_count_posts(self, instance):
        return instance.user_posts.all().count()

    def get_count_subscribers(self, instance):
        return instance.subscribers.all().count()

    def get_count_subscriptions(self, instance):
        return instance.subscriptions.all().count()

    def get_count_favorites(self, instance):
        return instance.favorites.all().count()