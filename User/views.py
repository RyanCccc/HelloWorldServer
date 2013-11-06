import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def login(request):
    params = json.loads(request.body)
    username = params.get('username')
    password = params.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse('success')
    else:
        return HttpResponse('fail')

def logout(request):
    pass

@csrf_exempt
def register(request):
    params = json.loads(request.body)
    username = params.get('username')
    password = params.get('password')
    user = None
    try:
        user = User.objects.create_user(username,password=password)
        if user:
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
    except:
        return HttpResponse('fail')
