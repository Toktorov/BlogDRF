from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    profile_image = models.ImageField(
        upload_to="profile_images/",
        verbose_name="Фотография профиля"
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст",
        blank = True, null = True
    )

    def __str__(self) -> str:
        return self.username 

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class UserFollower(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="subscriptions"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="subscribers"
    )

    def __str__(self):
        return f"From {self.from_user} - to {self.to_user}"

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
        unique_together = (('from_user', 'to_user'),)