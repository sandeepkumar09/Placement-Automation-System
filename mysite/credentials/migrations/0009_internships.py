# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0008_auto_20160308_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='internships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('field1', models.CharField(max_length=200, null=True)),
                ('field2', models.CharField(max_length=200)),
                ('field3', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
