# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class YouDao(models.Model):
    title = models.CharField('标题', max_length=256)
    channelName = models.CharField('分类', max_length=256)
    type = models.CharField('标签', max_length=256)
    url = models.CharField('内容链接', max_length=256)
    image_desk = models.CharField('图片链接', max_length=256)
    audiourl = models.CharField('音频链接', max_length=256)
    videourl = models.CharField('视频链接', max_length=256)
    time = models.CharField('创建时间', max_length=256)
    slug = models.CharField('slug', max_length=256, db_index=True)

    class Meta:
        verbose_name = "有道精选"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
