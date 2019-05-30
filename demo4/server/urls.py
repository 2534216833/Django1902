from django.conf.urls import url
from . import views

app_name = 'server'

urlpatterns = [
    url(r'^index/$',views.index, name='index'),
    url(r'^detail/(\d+)/$',views.detail, name='detail'),
    url(r'^blog/$',views.blog,name='blog'),
    url(r'^category/(\d+)/$', views.category, name='category'),
    url(r'^archives/(\d+)/(\d+)/$', views.archives, name='archives'),
    url(r'^tag/(\d+)/$',views.tag,name='tag')
]
