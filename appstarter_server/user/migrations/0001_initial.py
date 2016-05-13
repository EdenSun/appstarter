# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.IntegerField()),
                ('mobile', models.TextField(max_length=20)),
                ('email', models.TextField(max_length=50)),
                ('realName', models.TextField(max_length=20)),
                ('nickName', models.TextField(max_length=20)),
                ('qq', models.TextField(max_length=20)),
                ('wechat', models.TextField(max_length=20)),
                ('hobby', models.TextField(max_length=20)),
                ('introduction', models.TextField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
