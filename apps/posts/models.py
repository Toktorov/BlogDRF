from django.db import models

from apps.users.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_posts",
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class PostImages(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="post_images",
        verbose_name="Пост"
    )
    image = models.ImageField(
        upload_to="post_images/",
        verbose_name="Фотография"
    )
    
    def __str__(self):
        return f"{self.id}, {self.post}"

    class Meta:
        verbose_name = "Фотография к посту"
        verbose_name_plural = "Фотография к постам"

class PostComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="post_comment_user"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="post_comments",
        verbose_name="Пост"
    )
    comment = models.CharField(
        max_length=255,
        verbose_name="Текст комментарий"
    )
    self_comment = models.ForeignKey(
        'self', on_delete = models.SET_NULL,
        related_name = "post_self_comments",
        verbose_name="Ответ к комментарию",
        null = True, blank = True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.post}, {self.comment}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class PostLike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="post_likes",
        verbose_name="Пост"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="post_users",
        verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.post}, {self.user}"

    class Meta:
        verbose_name = "Лайки к посту"
        verbose_name_plural = "Лайки к постам"