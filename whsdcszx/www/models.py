# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Company_profile(models.Model):
    company_name = models.CharField(max_length=50, verbose_name='公司名称', default='武汉市水电测试中心')
    address = models.CharField(max_length=100, verbose_name='地址', default='武汉市江汉区水利路166号')
    phone_number = models.CharField(max_length=20, verbose_name='手机', default='13807117074')
    telephone = models.CharField(max_length=50, verbose_name='联系电话', default='027-83630193/83605046')
    fax = models.CharField(max_length=20, verbose_name='传真', default='027-83620432-803')
    url = models.CharField(max_length=50, verbose_name='网址', default='www.whsdcszx.com')
    profile = models.TextField(verbose_name='中心简介', default='')
    org_structure = models.TextField(max_length=1000, verbose_name='组织结构', null=True, blank=True)
    philosophy = models.TextField(verbose_name='经营理念', null=True, blank=True)
    business_info = models.TextField(verbose_name='业务介绍', default='')
    job = models.TextField(verbose_name='招聘信息', default='')
    account_titles = models.CharField(max_length=30, verbose_name='银行账户名', default='武汉市水电测试中心')
    bank_account = models.CharField(max_length=30, verbose_name='银行账号', default='17016701040003431（830186）')
    bank_name = models.CharField(max_length=30, verbose_name='银行', default='农行青年路支行')
    ibc_num = models.CharField(max_length=50, verbose_name='备案号', default='鄂ICP备14004256号')
    postcode = models.CharField(max_length=6, verbose_name='邮编', default='460015')

    class Meta:
        verbose_name = '公司资料'
        verbose_name_plural = '公司资料'

    def __unicode__(self):
        return '公司资料'


class Message(models.Model):
    title = models.CharField(max_length=50, verbose_name='主题')
    name = models.CharField(max_length=20, verbose_name='姓名')
    phone_number = models.CharField(max_length=20, verbose_name='联系电话')
    email = models.CharField(max_length=30, verbose_name='电子邮件')
    content = models.TextField(verbose_name='留言内容')
    time = models.DateTimeField(auto_created=True, auto_now=True,
                                verbose_name='留言时间')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '留言'

    def __unicode__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=30, verbose_name='主题')
    content = models.TextField(verbose_name='内容')
    date = models.DateField(auto_created=True, verbose_name='时间')
    count = models.IntegerField(default=0, verbose_name='点击次数')

    class Meta:
        verbose_name = '工程业绩'
        verbose_name_plural = '工程业绩'

    def __unicode__(self):
        return self.title


NEWS_TYPE = (
    ('1', '行业新闻'),
    ('2', '公司新闻')
)


class New(models.Model):
    title = models.CharField(max_length=30, verbose_name='主题')
    type = models.CharField(max_length=10, choices=NEWS_TYPE, verbose_name='新闻类型', default='2')
    content = models.TextField(verbose_name='新闻内容')
    date = models.DateField(auto_created=True, verbose_name='时间')
    count = models.IntegerField(default=0, verbose_name='点击次数')

    class Meta:
        verbose_name = '新闻资讯'
        verbose_name_plural = '新闻资讯'

    def __unicode__(self):
        return self.title


class Business(models.Model):
    type = models.CharField(max_length=50, verbose_name='业务类型')
    content = models.TextField(verbose_name='描述')

    class Meta:
        verbose_name = '业务类型'
        verbose_name_plural = '业务类型'

    def __unicode__(self):
        return self.type


class Qality_image(models.Model):
    name = models.CharField(max_length=100, verbose_name='资质图片名')
    image = models.ImageField(upload_to='qality_images', verbose_name='上传图片')

    class Meta:
        verbose_name = '资质图片'
        verbose_name_plural = '资质图片'

    def __unicode__(self):
        return self.name


class Carousel_image(models.Model):
    image = models.ImageField(upload_to='carousel_images', verbose_name='上传图片')

    class Meta:
        verbose_name = '首页轮播图片'
        verbose_name_plural = '首页轮播图片'

    def __unicode__(self):
        return self.image.name
