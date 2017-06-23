from django.conf.urls import url
from blogger.views import *

urlpatterns = [
    url(r'^$', post_list, name = 'blog'),
    url(r'^pop/$', post_list_views, name= 'popular'),
    url(r'^(?P<id>\d+)/$', post_detail, name="post_detail"),
    url(r'^post/new/$', new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', edit_post, name='edit'),
]