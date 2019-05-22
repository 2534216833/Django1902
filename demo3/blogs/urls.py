from django.conf.urls import url
from . import views

app_name = 'blogs'

urlpatterns = [

    url(r'^detail/(\d+)/$', views.detail, name='detail'),

    url(r'^index/$', views.index , name='index'),
]
