# Generated by Django 4.2.2 on 2023-06-27 05:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='showers',
            field=models.ManyToManyField(related_name='lesson_showers', to=settings.AUTH_USER_MODEL),
        ),
    ]