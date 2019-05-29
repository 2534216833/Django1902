from django.conf.urls import url
from . import views

app_name = 'server'

urlpatterns = [
    url(r'^index/$',views.index, name='index'),
    url(r'^detail/$',views.detail, name='detail'),

]
