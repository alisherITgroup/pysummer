# Generated by Django 4.2.2 on 2023-06-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_problem_attempt_lesson_problems'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='status',
            field=models.CharField(blank=True, default='Running', max_length=20, null=True),
        ),
    ]
