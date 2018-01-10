# -*- coding:utf-8 -*-
from django.contrib import admin
from models import New
import models


# Register your models here.

class New_Admin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/tinymce/js/jquery.mini.js',
            '/static/tinymce/js/tinymce/tinymce.min.js',
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',
            '/static/tinymce/js/tinymce/textarea.js',
        ]


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'name', 'phone', 'email', 'time')

    list_per_page = 50

    ordering = ('-time',)

    list_display_links = ['id', 'title', 'content']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(New, New_Admin)
admin.site.register(models.Message, MessageAdmin)
