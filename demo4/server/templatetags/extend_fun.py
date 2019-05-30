from django import template
from ..models import Ads,Tag,CateGory,Article


register = template.Library()

@register.simple_tag
def getads():
    return Ads.objects.all()


@register.simple_tag
def gettags():
    return Tag.objects.all()


@register.simple_tag(name='getcategorys')
def getcategorys():
    return CateGory.objects.all()


@register.simple_tag
def getarchives(num = 3):
    result =  Article.objects.dates("creat_time",'month',order="DESC")[:num]
    return result


@register.filter(name='myslice')
def myslice(value,length):
    result = value[:length]
    return  result
