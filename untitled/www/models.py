# -*-coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.safestring import mark_safe


# Create your models here.

class New(models.Model):
    title = models.CharField(verbose_name='标题', max_length=20, default='')
    content = models.TextField(verbose_name='内容', max_length=1000, default='')
    date = models.DateField(verbose_name='日期', auto_created=True)

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'

    def __unicode__(self):
        return self.title


class Images(models.Model):
    name = models.CharField(max_length=30, verbose_name='图片名')
    image = models.ImageField(upload_to='images', verbose_name='上传图片')

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px" />' % obj.image.url)

    # 页面显示的字段名称
    image_data.short_description = u'图片'


class Message(models.Model):
    title = models.CharField(max_length=30,verbose_name='主题')
    name = models.CharField(max_length=30,verbose_name='名字')
    phone = models.CharField(max_length=30,verbose_name='联系电话')
    email = models.CharField(max_length=30,verbose_name='电子邮件')
    content = models.TextField(max_length=1000,verbose_name='留言内容')
    time = models.DateTimeField(auto_created=True, auto_now=True,verbose_name='时间')

    def __unicode__(self):
        return self.title


