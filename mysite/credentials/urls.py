from django.conf.urls import patterns, url

urlpatterns = patterns('credentials.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^clist/$', 'clist', name='clist'),
)