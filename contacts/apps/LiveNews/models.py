# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.


# 网易新闻
class WangYi(models.Model):
    title = models.CharField('标题', max_length=256, null=True)
    platform = models.CharField('平台', max_length=256, null=True)
    type = models.CharField('类型', max_length=256, null=True)
    url = models.CharField('内容链接', max_length=256, null=True)
    imageurl = models.CharField('图片链接', max_length=256, null=True)
    audiourl = models.CharField('音频链接', max_length=256, null=True)
    videourl = models.CharField('视频链接', max_length=256, null=True)
    time = models.CharField('创建时间', max_length=256, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    id = models.IntegerField('id', db_index=True, default='', primary_key=True)

    class Meta:
        verbose_name = "网易新闻"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


# 腾讯新闻
class TengXun(models.Model):
    title = models.CharField('标题', max_length=256, null=True)
    platform = models.CharField('平台', max_length=256, null=True)
    type = models.CharField('类型', max_length=256, null=True)
    url = models.CharField('内容链接', max_length=256, null=True)
    imageurl = models.CharField('图片链接', max_length=256, null=True)
    audiourl = models.CharField('音频链接', max_length=256, null=True)
    videourl = models.CharField('视频链接', max_length=256, null=True)
    time = models.CharField('创建时间', max_length=256, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    id = models.IntegerField('id', db_index=True, default='', primary_key=True)

    class Meta:
        verbose_name = "腾讯新闻"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title