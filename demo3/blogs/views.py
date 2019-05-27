from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from.models import Article,CateGory,Tag
from django.core.paginator import Paginator
import markdown
from comment.forms import CommentForm
from django.views.generic import View
from .forms import ContactForm
from django.core.mail import  send_mail, send_mass_mail,settings

# Create your views here.
def index(request):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum
    articles = Article.objects.all().order_by("-views")
    paginator = Paginator(articles,2)
    page = paginator.get_page(pagenum)
    return render(request,'index.html',{"page":page})


def detail(request,id):

    article = get_object_or_404(Article,pk = id)

    #阅读数
    article.views +=1
    article.save()



    # 使用markdown处理body  将markdown语法转换为html标签

    # 第一种使用  针对需要处理的article.body 将markdown转为html'
    # article.body = markdown.markdown(article.body, extensions = [
    #
    #     "markdown.extensions.extra",
    #     "markdown.extensions.codehilite",
    #     "markdown.extensions.toc"
    #
    # ])

    # 第二种如果在外部使用目录  需要使用构造函数的写法
    mk = markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc"
    ])
    article.body = mk.convert(article.body)

    article.toc = mk.toc

    cf = CommentForm()

    return render(request,'single.html',locals())

def archives(request,year,month):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = Article.objects.filter(creat_time__year=year, creat_time__month=month)
    paginator = Paginator(articles, 1)

    # 传入页码得到一个页面   page包含所有信息

    page = paginator.get_page(pagenum)

    page.parms = "/archives/%s/%s/" % (year, month)
    return render(request, 'index.html', {"page": page})


def category(request,id):

    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(CateGory,pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/category/%s/"%(id,)
    return render(request, 'index.html', {"page": page })


def tag(request,id):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(Tag, pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/tag/%s/"%(id,)
    return render(request, 'index.html', {"page": page})


class Contacts(View):
    def get(self,request):
        cf = ContactForm()
        return render(request, 'contact.html',locals())
    def post(self,request):
        from django.conf import settings
        send_mail("xxxxxxx" ,"yyyyyyyyyy",settings.DEFAULTFROMEMAIL,["2534216833@qq.com","2953957576@qq.com"])

        cf = ContactForm(request.POST)
        cf.save()
        cf = ContactForm()
        return render(request, 'contact.html', {"info":'成功',"cf":cf})























