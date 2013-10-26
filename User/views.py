from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    params = request.POST
    username = params.get('username')
    password = params.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse('success')
    else:
        return HttpResponse('fail')

def logout(request):
    pass

def register(request):
    params = request.POST
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
