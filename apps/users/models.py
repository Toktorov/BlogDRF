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
    )

    def __str__(self) -> str:
        return self.username 

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"