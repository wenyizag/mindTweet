# Generated by Django 2.1 on 2018-08-21 21:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0007_auto_20180817_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]