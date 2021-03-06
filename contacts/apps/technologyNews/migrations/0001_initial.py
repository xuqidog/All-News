# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-26 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouDao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('channelName', models.CharField(max_length=256, verbose_name='\u5206\u7c7b')),
                ('type', models.CharField(max_length=256, verbose_name='\u6807\u7b7e')),
                ('url', models.CharField(max_length=256, verbose_name='\u5185\u5bb9\u94fe\u63a5')),
                ('image_desk', models.CharField(max_length=256, verbose_name='\u56fe\u7247\u94fe\u63a5')),
                ('audiourl', models.CharField(max_length=256, verbose_name='\u97f3\u9891\u94fe\u63a5')),
                ('videourl', models.CharField(max_length=256, verbose_name='\u89c6\u9891\u94fe\u63a5')),
                ('time', models.CharField(max_length=256, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='slug')),
            ],
            options={
                'verbose_name': '\u6709\u9053\u7cbe\u9009',
                'verbose_name_plural': '\u6709\u9053\u7cbe\u9009',
            },
        ),
    ]
