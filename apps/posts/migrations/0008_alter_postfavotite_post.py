# Generated by Django 4.1.5 on 2023-01-20 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_postfavotite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfavotite',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_favotites', to='posts.post', verbose_name='Пост'),
        ),
    ]