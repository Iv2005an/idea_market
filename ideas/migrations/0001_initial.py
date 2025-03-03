# Generated by Django 5.1.6 on 2025-02-21 07:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('votes', models.IntegerField(default=0, verbose_name='Голоса')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
