# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *


class MyAdminSite(admin.AdminSite):
    site_header = '武汉水电测试中心管理系统'  # 此处设置页面显示标题
    site_title = '武汉水电测试中心管理系统'  # 此处设置页面头部标题


admin_site = MyAdminSite(name='management')


class QalityImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_data')
    readonly_fields = ('image_data',)
    list_display_links = ('name', 'image_data')

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="250px" />' % obj.image.url)

    image_data.short_description = '资质图片'


class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('image_data',)
    list_display_links = ['image_data']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="500px" height="150" title="点击修改" />' % obj.image.url)

    image_data.short_description = '轮播图片'


class NewAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/tinymce/js/jquery.min.js',  # 必须首先加载的jquery，手动添加文件
            '/static/tinymce/js/tinymce/tinymce.min.js',  # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',  # 手动添加文件
            '/static/tinymce/js/tinymce/textarea.js',  # 手动添加文件，用户初始化参数
        ]


class ProjectAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/tinymce/js/jquery.min.js',  # 必须首先加载的jquery，手动添加文件
            '/static/tinymce/js/tinymce/tinymce.min.js',  # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',  # 手动添加文件
            '/static/tinymce/js/tinymce/textarea.js',  # 手动添加文件，用户初始化参数
        ]


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'name', 'phone_number', 'email', 'time')

    list_per_page = 50

    ordering = ('-time',)

    list_display_links = ['id', 'title', 'content']

    def has_add_permission(self, request):
        return False

        # def has_change_permission(self, request, obj=None):
        #     return False


class ProfileAdmin(admin.ModelAdmin):
    fields = ('company_name', 'address', 'profile', 'business_info', 'job', 'phone_number', 'telephone', 'fax', 'url',
              'account_titles', 'bank_account', 'bank_name', 'ibc_num', 'postcode')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# Register your models here.

admin.site.register([Business])
admin.site.register(Carousel_image, CarouselImageAdmin)
admin.site.register(Qality_image, QalityImageAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Company_profile, ProfileAdmin)
