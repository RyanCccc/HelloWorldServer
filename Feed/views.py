import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Feed.models import Feed, Reply

# Create your views here.
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
    except Exception as e:
        print e
        return HttpResponse(-1)


def get(request):
    pass


def get_list(request):
    pass


def remove(request):
    pass


def add_reply(request):
    pass


def remove_reply(request):
    pass


def get_reply(request):
    pass


def like(request):
    pass


def dislike(request):
    pass
