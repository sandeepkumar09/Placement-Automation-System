# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]