from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from www.models import Message


@csrf_exempt
def message(request):
    if request.method == 'GET':
        return render_to_response('message.html')
    if request.method == 'POST':
        message = Message(name=request.POST['name'], title=request.POST['title'], phone=request.POST['phone'],
                          email=request.POST['email'], content=request.POST['content'])
        message.save()
        return JsonResponse({"data": "success"})
