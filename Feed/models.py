import datetime

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


class Reply(models.Model):
    user = models.ForeignKey(User)
    feed = models.ForeignKey(Feed)
    content = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.datetime.now)
