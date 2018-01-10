# -*-coding:utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
import json
import time
from models import *
from PIL import Image
from django.conf import settings
from django.http import HttpResponse, JsonResponse
import os

# Create your views here.

static_base = 'http://127.0.0.1:8000'
static_url = static_base + settings.MEDIA_URL  # 上传文件展示路径前缀


# 上传图片 POST
@csrf_exempt
def upload_img(request):
    file = request.FILES['file']
    data = {
        'error': True,
        'path': '',
    }
    if file:
        timenow = int(time.time() * 1000)
        timenow = str(timenow)
        try:
            img = Image.open(file)
            img.save(settings.MEDIA_ROOT + "content/" + timenow + os.path.splitext(str(file))[1])
        except Exception, e:
            print e
            return HttpResponse(json.dumps(data), content_type="application/json")
        imgUrl = static_url + 'content/' + timenow + os.path.splitext(str(file))[1]
        data['error'] = False
        data['path'] = imgUrl
    return HttpResponse(json.dumps(data), content_type="application/json")


def index(request):
    news_list = New.objects.order_by("-date")[:7].values("id", "title")
    quality_image = Qality_image.objects.all()
    common_data = common()
    return render_to_response('index.html',
                              dict({"news_list": news_list, 'qulity_image': quality_image}, **common_data))


def common():
    carousel = Carousel_image.objects.all()[:3]
    profile = Company_profile.objects.get()
    return {'carousel': carousel, 'profile': profile}


def news(request):
    news_list = New.objects.all()
    paginator = Paginator(news_list, 15)
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        new = paginator.page(1)
    except EmptyPage:
        new = paginator.page(paginator.num_pages)
    business_list = Business.objects.all()
    return render_to_response('news.html', dict({'news_list': new, 'business_list': business_list}, **common()))


def news_1(request):
    news_list = New.objects.all().filter(type='1')
    paginator = Paginator(news_list, 15)
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        new = paginator.page(1)
    except EmptyPage:
        new = paginator.page(paginator.num_pages)
    business_list = Business.objects.all()
    return render_to_response('news_1.html', dict({'news_list': new, 'business_list': business_list}, **common()))


def news_2(request):
    news_list = New.objects.all().filter(type='2')
    paginator = Paginator(news_list, 15)
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        new = paginator.page(1)
    except EmptyPage:
        new = paginator.page(paginator.num_pages)
    business_list = Business.objects.all()
    return render_to_response('news_2.html', dict({'news_list': new, 'business_list': business_list}, **common()))


def news_details(request, id):
    news = New.objects.get(id=id)
    news.count = news.count + 1
    news.save()
    business_list = Business.objects.all()
    return render_to_response('news_details.html', dict({'news': news, 'business_list': business_list}, **common()))


def project_details(request, id):
    project = Project.objects.get(id=id)
    project.count = project.count + 1
    project.save()
    business_list = Business.objects.all()
    return render_to_response('project_details.html',
                              dict({'project': project, 'business_list': business_list}, **common()))


def profile(request):
    profile = Company_profile.objects.get()
    business = Business.objects.all()
    return render_to_response('profile.html', dict({'business': business, 'profile': profile}, **common()))


def business_type(request, id):
    profile = Company_profile.objects.get()
    business = Business.objects.get(id=id)
    business_list = Business.objects.all()
    return render_to_response('business_type.html',
                              dict({'business': business, 'business_list': business_list, 'profile': profile},
                                   **common()))


def business(request):
    profile = Company_profile.objects.get()
    business = Business.objects.all()
    return render_to_response('business.html', dict({'business_list': business, 'profile': profile}, **common()))


def project(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 15)
    page = request.GET.get('page')
    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        project = paginator.page(1)
    except EmptyPage:
        project = paginator.page(paginator.num_pages)
    business_list = Business.objects.all()
    return render_to_response('project.html',
                              dict({'project_list': project, 'business_list': business_list}, **common()))


@csrf_exempt
def message(request):
    if request.method == 'GET':
        business_list = Business.objects.all()
        return render_to_response('message.html', dict({'business_list': business_list}, **common()))
    if request.method == 'POST':
        message = Message(name=request.POST['name'], title=request.POST['title'], phone_number=request.POST['phone'],
                          email=request.POST['email'], content=request.POST['content'])
        message.save()
        return JsonResponse({"data": "success"})


def contact_us(request):
    business_list = Business.objects.all()
    return render_to_response('contact_us.html',
                              dict({'business_list': business_list}, **common()))


def jobs(request):
    business_list = Business.objects.all()
    return render_to_response('jobs.html',
                              dict({'business_list': business_list}, **common()))


def zizhi(request):
    zizhi_list = Qality_image.objects.all()
    business_list = Business.objects.all()
    return render_to_response('zizhi.html',
                              dict({'business': business_list, 'zizhi_list': zizhi_list}, **common()))
