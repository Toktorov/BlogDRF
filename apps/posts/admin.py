from django.contrib import admin

from apps.posts.models import Tag, Post, PostComment, PostImages, PostLike, PostFavotite

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostImages)
admin.site.register(PostLike)
admin.site.register(PostFavotite)