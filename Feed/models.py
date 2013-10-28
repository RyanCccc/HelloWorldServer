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

    def get_json(self):
        data = {}
        data['username']=self.user.username
        data['content']=self.content
        data['date']=str(self.date)
        data['latitude']=self.latitude
        data['longitude']=self.longitude
        data['likes']=self.likes
        data['dislikes']=self.dislikes
        return json.dumps(data)

class Reply(models.Model):
    user = models.ForeignKey(User)
    feed = models.ForeignKey(Feed)
    content = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.datetime.now)
