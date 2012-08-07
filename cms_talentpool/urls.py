from django.conf.urls.defaults import *
from .views import show_talent_pool, show_talent

urlpatterns = patterns('',
    url(r'^$', show_talent_pool, name='show_talent_pool'),
    url(r'^(?P<talent_slug>[-\w]+)/$', show_talent, name='show_talent'),
)