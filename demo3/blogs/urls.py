from django.conf.urls import url
from . import views
from . import feed
app_name = 'blogs'

urlpatterns = [

    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^archives/(\d+)/(\d+)/$',views.archives,name='archives'),
    url(r'^category/(\d+)/$',views.category,name='category'),
    url(r'^index/$', views.index , name='index'),
    url(r'^tag/(\d+)/$',views.tag,name='tag'),
    url(r'^rss/$',feed.BlogFeed(),name='rss'),
    url(r'^contactus/$', views.Contacts.as_view(), name='contactus'),
]
