# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-26 12:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('credentials', '0021_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=20)),
                ('dob', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_type',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_type',
        ),
    ]
