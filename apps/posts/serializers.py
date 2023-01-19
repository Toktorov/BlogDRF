from rest_framework import serializers

from apps.posts.models import Post, PostImages, PostComment, PostLike

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = "__all__"

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = "__all__"

class PostDetailSerializer(serializers.ModelSerializer):
    post_likes = PostLikeSerializer(read_only = True, many = True)
    count_likes = serializers.SerializerMethodField(read_only = True)
    post_comments = PostCommentSerializer(read_only = True, many = True)
    count_comments = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created', 'user', 'count_likes', 'post_likes', 'post_comments', 'count_comments')

    def get_count_likes(self, instance):
        return instance.post_likes.all().count()

    def get_count_comments(self, instance):
        return instance.post_comments.all().count()

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description')