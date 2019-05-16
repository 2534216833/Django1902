from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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

    temp2=loader.get_template('booktest/detail.html')
    result=temp2.render({ 'book':book })
    return HttpResponse(result)
def deletebook(request,id):
    # return HttpResponse("成功")
    BookInfo.objects.get(pk=id).delete()
    return HttpResponseRedirect("/booktest/list/")


def deletehero(request,id):
    # return HttpResponse("成功")
    hero=HeroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    return HttpResponseRedirect("/booktest/detail/%s/"%(bookid,))



# 添加人物
def addhero(request,id):
    if request.method == "GET":
        return render(request, "booktest/addhero.html",
                      {'bookid': id})
    elif request.method == "POST":
        book=BookInfo.objects.get(pk = id)
        hero=HeroInfo()
        hero.name=request.POST["username"]
        value=request.POST['sex']
        hero.gender=value
        hero.skill=request.POST['skill']
        hero.book = book

        hero.save()

        return HttpResponseRedirect("/booktest/detail/%s"%(id,))



# 添加书籍

def addbook(request):
    if request.method == "GET":
        return render(request, "booktest/addbook.html")

    elif request.method == "POST":

        addbook=BookInfo()
        title=request.POST['bookname']
        print(title,'title')
        addbook.title=title
        pub_date=request.POST['booktime']
        print(pub_date,)
        addbook.pub_date=pub_date



        addbook.save()

        return HttpResponseRedirect("/booktest/list")








