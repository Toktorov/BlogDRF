from rest_framework import serializers

from apps.posts.models import Post, PostImages, PostComment, PostLike

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = "__all__"

class LikeSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

class PostDetailSerializer(serializers.ModelSerializer):
    post_likes = LikeSerilaizer(read_only = True, many = True)
    count_likes = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created', 'user', 'count_likes', 'post_likes')

    def get_count_likes(self, instance):
        return instance.post_likes.all().count()

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description')

    def create(self):
        post = Post.objects.create(user = self.context['request'].user, title = self.initial_data['title'], description = self.initial_data['description'])
        return post