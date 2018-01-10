# -*- coding: utf-8 -*-
"""whsdcszx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from www import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^news/(?P<id>\d+)$', views.news_details),
    url(r'^news/$', views.news),
    url(r'^news_1/$', views.news_1),
    url(r'^news_2/$', views.news_2),
    url(r'^project/$', views.project),
    url(r'^project/(?P<id>\d+)$', views.project_details),
    url(r'^profile/$', views.profile),
    url(r'business/(?P<id>\d+)$', views.business_type),
    url(r'^upload_img/$', views.upload_img),  # 后台富文本框上传图片
    url(r'^business/$', views.business),
    url(r'^message/$', views.message),
    url(r'^contact_us/$', views.contact_us),
    url(r'^jobs/$', views.jobs),
    url(r'^zizhi/$', views.zizhi),
    url(r'^admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
