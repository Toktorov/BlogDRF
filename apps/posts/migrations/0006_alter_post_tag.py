# Generated by Django 4.1.5 on 2023-01-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_tag_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='posts_tag', to='posts.tag'),
        ),
    ]