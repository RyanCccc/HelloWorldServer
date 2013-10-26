from django.conf.urls import patterns, include, url

urlpatterns = patterns('Feed.views',
    # Examples:
    # url(r'^$', 'PCS.views.home', name='home'),
    # url(r'^PCS/', include('PCS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^create/$', 'create',
        name = 'feed_create'),
    url(r'^get/$', 'get',
        name = 'feed_get'),
    url(r'^get_list/$', 'get_list',
        name = 'feed_get_list'),
    url(r'^remove/$', 'remove',
        name = 'feed_remove'),
    url(r'^add_reply/$', 'add_reply',
        name = 'feed_add_reply'),
    url(r'^remove_reply/$', 'remove_reply',
        name = 'feed_remove_reply'),
    url(r'^get_reply/$', 'get_reply',
        name = 'feed_get_reply'),
    url(r'^like/$', 'like',
        name = 'feed_like'),
    url(r'^dislike/$', 'dislike',
        name = 'feed_dislike'),
)
