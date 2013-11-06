import datetime
import json

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
    user = models.ForeignKey(User)
    content = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.datetime.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

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

    @classmethod
    def get_json_list(self):
        data = []
        feeds = self.objects.all()
        for feed in feeds:
            data.append(feed.get_json(get_data=True))
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
        except Exception as e:
            raise e

class Reply(models.Model):
    user = models.ForeignKey(User)
    feed = models.ForeignKey(Feed)
    content = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.datetime.now)
