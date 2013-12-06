import datetime
import json

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from util import distance_on_unit_sphere

# Create your models here.
class Feed(models.Model):
    user = models.ForeignKey(User)
    content = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.datetime.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __repr__(self):
        return self.content

    def __str__(self):
        return self.content

    def get_json(self, get_data=False):
        data = {}
        data['id']=self.pk
        data['username']=self.user.username
        data['content']=self.content
        data['date']=str(self.date)
        data['latitude']=self.latitude
        data['longitude']=self.longitude
        data['likes']=self.likes
        data['dislikes']=self.dislikes
        if get_data:
            return data
        return json.dumps(data)

    def get_reply_json_list(self):
        data = []
        replies = self.reply_set.all()
        for reply in replies:
            data.append(reply.get_json(get_data=True))
        return json.dumps(data)

    def add_reply_by_json(self, post_json):
        try:
            user = User.objects.get(username=post_json.get('username'))
            content = post_json.get('content')
            reply = Reply.objects.create(
                user = user,
                feed = self,
                content = content,
            )
        except Exception as e:
            raise e

    @classmethod
    def get_json_list(self, _filter, get_data=False):
        data = []
        feeds = self.objects.filter(likes__gte=_filter['likes'])
        for feed in feeds:
            if distance_on_unit_sphere(
                feed.latitude,
                feed.longitude,
                _filter['latitude'],
                _filter['longitude']
            ) < _filter['_range'] and feed.reply_set.count() >= _filter['num_reply']:
                data.append(feed.get_json(get_data=True))
        if get_data:
                return data
        return json.dumps(data)

    @classmethod
    def create_by_json(self, post_json):
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
            from gcm.models import get_device_model
            phones = get_device_model().objects.all()
            for phone in phones:
                phone.send_message('New Feed Available!')
        except Exception as e:
            raise e

class Reply(models.Model):
    user = models.ForeignKey(User)
    feed = models.ForeignKey(Feed)
    content = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return self.content

    def __str__(self):
        return self.content

    def get_json(self, get_data=False):
            data = {}
            data['id']=self.pk
            data['username']=self.user.username
            data['feed_id']=self.feed.pk
            data['content']=self.content
            data['date']=str(self.date)
            if get_data:
                return data
            return json.dumps(data)

admin.site.register(Feed)
admin.site.register(Reply)
