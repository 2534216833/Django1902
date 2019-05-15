from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from  .models import BookInfo,HeroInfo
# Create your views here.
def index(request):



    # return HttpResponse("index首页")
    template=loader.get_template('booktest/index.html')

    contex={}

    result=template.render(contex)
    return HttpResponse(result)

def list(request):

    allbook=BookInfo.objects.all()
    # return HttpResponse("list列表页")
    temp1=loader.get_template('booktest/list.html')
    result=temp1.render({ 'allbook':allbook })
    return HttpResponse(result)
def detail(request,id):
    book=None
    try:
        book=BookInfo.objects.get(pk = id)
    except Exception as e:
        return HttpResponse("没有书籍信息111,%s"%book)

    temp2=loader.get_template('booktest/detali.html')
    result=temp2.render({ 'book':book })
    return HttpResponse(result)