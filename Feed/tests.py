"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from models import Feed, Reply

class SimpleTest(TestCase):
    def setUp(self):
        user = User.objects.create_user("ryanc",password="123456")
        for i in range(0,10):
            content = 'this is a test ' + str(i) 
            latitude = 0
            longitude = 0
            if i==0:
                latitude = 60.989522
                longitude = -149.61745
            likes = 30
            dislikes = 0
            feed = Feed.objects.create(
                user = user,
                content = content,
                latitude = latitude,
                longitude = longitude,
                likes = likes,
                dislikes = dislikes,
            )

    def test_get_json_list(self):
        self.assertEqual(Feed.objects.count(),10)
        _filter = {}
        _filter['_range']=100
        _filter['likes']=20
        _filter['latitude']=60.98933
        _filter['longitude']=-149.61693
        _filter['num_reply']=0
        feeds = Feed.get_json_list(_filter, get_data=True)
        self.assertEqual(len(feeds),1)
