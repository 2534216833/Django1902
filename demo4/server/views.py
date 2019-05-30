from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from django.core.paginator import Paginator
import markdown
from django.views.generic import View
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
from django.views.decorators.cache import cache_page

#  Paginator  Page

# Create your views here.


def index(request):
    img =  Picture.objects.all()
    title    = Title.objects.all()
    articles = Brief.objects.all()
    staff = Staffimage.objects.all()
    if request.method == "POST":
        username  = request.POST["username"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        news = request.POST["news"]
        strA = "姓名：%s ，电话：%s，邮箱：%s，内容：%s"%(username,phone,email,news)
        send_mail("信息", "%s"%strA, settings.DEFAULT_FROM_EMAIL,
                  ["2953957576@qq.com", "2534216833@qq.com"])
        info='成功'
        return render(request, 'index.html',locals())


    # staffimg =Staffimage.objects.all()
    # for i in articles:
    #     print(i.title)
    return render(request,'index.html',locals())


def detail(request,id):

    article = get_object_or_404(Article, pk= id )


    return render(request,'detail.html',locals())

def blog(request):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum
    # 得到所有文章
    articles = Article.objects.all().order_by("-views")
    paginator = Paginator(articles, 4)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    return render(request, 'blog.html', {"page": page})

def category(request,id):

    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(CateGory,pk=id).article_set.all()
    paginator = Paginator(articles, 4)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/category/%s/"%(id,)
    return render(request, 'blog.html', {"page": page })

def archives(request,year,month):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = Article.objects.filter(creat_time__year=year, creat_time__month=month)
    paginator = Paginator(articles, 1)

    # 传入页码得到一个页面   page包含所有信息

    page = paginator.get_page(pagenum)

    page.parms = "/archives/%s/%s/" % (year, month)
    return render(request, 'blog.html', {"page": page})

def tag(request,id):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(Tag, pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/tag/%s/"%(id,)
    return render(request, 'blog.html', {"page": page})