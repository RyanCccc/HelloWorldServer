import os
import sys
     
path = '/srv/project/HelloWorldServer'
if path not in sys.path:
    sys.path.insert(0, '/srv/project/HelloWorldServer')
     
os.environ['DJANGO_SETTINGS_MODULE'] = 'HelloWorldServer.settings'
     
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
