# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

# 36kr
class kr(models.Model):
    title = models.CharField('标题', max_length=256)
    summary = models.CharField('简介', max_length=256)
    extraction_tags = models.CharField('分类', max_length=256)
    column_name = models.CharField('标签', max_length=256)
    cover = models.CharField('图片链接', max_length=256)
    published_at = models.CharField('创建时间', max_length=256)
    id = models.IntegerField('id', db_index=True, primary_key=True)

    class Meta:
        verbose_name = "36kr"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


# 硅谷密探
class svinsight(models.Model):
    title = models.CharField('标题', max_length=256)
    summary = models.CharField('简介', max_length=256)
    tags = models.CharField('分类', max_length=256)
    cover = models.CharField('图片链接', max_length=256)
    add_time = models.CharField('创建时间', max_length=256)
    url = models.CharField('url', max_length=256)

    class Meta:
        verbose_name = "硅谷密探"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title