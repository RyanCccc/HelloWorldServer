import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from Feed.models import Feed, Reply
from django.core import exceptions

ObjectDoesNotExist = -1
ParseError = -2

# Create your views here.
@csrf_exempt
def create(request):
    post_json = json.loads(request.body)
    try:
        user = User.objects.get(username=post_json.get('username'))
        content = post_json.get('content')
        latitude = post_json.get('latitude')
        longitude = post_json.get('longitude')
        likes = post_json.get('likes')
        dislikes = post_json.get('dislikes')
        feed = Feed.objects.create(
            user = user,
            content = content,
            latitude = latitude,
            longitude = longitude,
            likes = likes,
            dislikes = dislikes,
        )
        return HttpResponse(feed.pk)
    except exceptions.ObjectDoesNotExist as e:
        return HttpResponse(ObjectDoesNotExist)
    except Exception as e:
        return HttpResponse(ParseError)


@csrf_exempt
def get(request):
    post_json = json.loads(request.body)
    try:
        pk = post_json.get('id')
        feed = Feed.objects.get(pk=pk)
        return HttpResponse(feed.get_json())
    except exceptions.ObjectDoesNotExist as e:
        return HttpResponse(ObjectDoesNotExist)
    except Exception as e:
        return HttpResponse(ParseError)


@csrf_exempt
def get_list(request):
    post_json = json.loads(request.body)
    _filter = {}
    result = ''
    try:
        _filter['_range'] = post_json.get('range')
        _filter['latitude'] = post_json.get('latitude')
        _filter['longitude'] = post_json.get('longitude')
        _filter['likes'] = post_json.get('likes')
        _filter['num_reply'] = post_json.get('num_reply')
        result = Feed.get_json_list(_filter=_filter)
    except Exception as e:
        return HttpResponse(ParseError)
    return HttpResponse(result)


@csrf_exempt
def remove(request):
    pass


@csrf_exempt
def add_reply(request):
    post_json = json.loads(request.body)
    try:
        pk = post_json.get('feed_id')
        feed = Feed.objects.get(pk=pk)
        feed.add_reply_by_json(post_json)
        return HttpResponse('success')
    except exceptions.ObjectDoesNotExist as e:
        return HttpResponse('fail')
    except Exception as e:
        return HttpResponse('fail')


@csrf_exempt
def remove_reply(request):
    pass


@csrf_exempt
def get_reply(request):
    post_json = json.loads(request.body)
    try:
        pk = post_json.get('feed_id')
        feed = Feed.objects.get(pk=pk)
        return HttpResponse(feed.get_reply_json_list())
    except exceptions.ObjectDoesNotExist as e:
        return HttpResponse('fail')
    except Exception as e:
        return HttpResponse('fail')


@csrf_exempt
def like(request):
    post_json = json.loads(request.body)
    try:
        pk = post_json.get('id')
        feed = Feed.objects.get(pk=pk)
        feed.likes += 1
        feed.save()
        return HttpResponse('success')
    except exceptions.ObjectDoesNotExist as e:
        return HttpResponse('fail')
    except Exception as e:
        return HttpResponse('fail')


@csrf_exempt
def dislike(request):
    post_json = json.loads(request.body)
    try:
        pk = post_json.get('id')
        feed = Feed.objects.get(pk=pk)
        feed.dislikes += 1
        feed.save()
        return HttpResponse('success')
    except exceptions.ObjectDoesNotExist as e:
        return HttpResponse('fail')
    except Exception as e:
        return HttpResponse('fail')
