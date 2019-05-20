from django.conf.urls import url
from . import views



app_name='vote'

urlpatterns=[
    # url(r'^list/$', views.list, name="list"),
    url(r'^index/$',views.index,name='index'),
    url(r'^votingpage/(\d+)/$',views.VotingPage,name='votingpage'),
    url(r'^votingresult/(\d+)/$',views.VotingResult,name='votingresult')
]
