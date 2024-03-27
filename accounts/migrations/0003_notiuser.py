# Generated by Django 5.0.3 on 2024-03-26 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_email_remove_userprofile_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotiUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=225)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('token_bot', models.CharField(blank=True, max_length=225)),
                ('chat_id', models.CharField(blank=True, max_length=225)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
