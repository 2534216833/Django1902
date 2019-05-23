from django import template
from ..models import Article,CateGory,Tag

register = template.Library()

@register.filter(name='mylower')
def mylower(value):
    return value.lower()

@register.filter(name='myslice')
def myslice(value,length):
    result = value[:length]
    return  result

@register.simple_tag(name='getcategorys')
def getcategorys():
    return CateGory.objects.all()


@register.simple_tag
def getlatestarticles(num = 3):
    return Article.objects.all().order_by("-creat_time")[:num]

@register.simple_tag
def getarchives(num = 3):
    result =  Article.objects.dates("creat_time",'month',order="DESC")[:num]
    return result

@register.simple_tag
def gettags():
    return Tag.objects.all()

















