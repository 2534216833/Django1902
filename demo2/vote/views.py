from .forms import LoginForm,RegisterForm
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.generic import View
from  .models import VoteContent,Vote,MyUser
from .util import checklogin
from django.contrib.auth import authenticate,login as lgi,logout as lgo

# Create your views here.

# 查看投票信息

# @checklogin
# def index(request):
#     allvote=VoteContent.objects.all()
#     username = request.session.get('username')
#     temp1=loader.get_template('vote/index.html')
#     result=temp1.render({'allvote':allvote})
#     print(username)
#     return HttpResponse(result)

#
@checklogin
def index(request):
    username = request.session.get('username')
    print(username)
    allvote = VoteContent.objects.all()
    return render(request,'vote/index.html', locals())


# 投票选择界面

@checklogin
def VotingPage(request,id):

    voting = VoteContent.objects.get(pk=id)

    if request.method == "GET":
        temp = loader.get_template('vote/votingpage.html')
        result = temp.render({'voting': voting})
        return render(request, "vote/votingpage.html", {'voting': voting},)

    elif request.method == "POST":

        temp4 = voting.vote_set.all()
        t1=temp4[0].id
        temp3 = Vote.objects.get(pk=t1)
        x = request.POST['sex']
        if x == '1':
            temp3.Poll_1 += 1
            temp3.save()
            return HttpResponseRedirect("/vote/votingresult/%s" % (t1,))
        else:
            temp3.Poll_2 += 1
            temp3.save()
            return HttpResponseRedirect("/vote/votingresult/%s" % (t1,))


@checklogin
def VotingResult(request,id):


    Vresult = Vote.objects.get(pk=id)

    allvote=VoteContent.objects.all()

    temp=loader.get_template('vote/votingresult.html')
    result=temp.render({ 'Vresult':Vresult,'allvote':allvote})

    return HttpResponse(result)




#退出
def logout(request):
    res = redirect(reverse('vote:login'))
    lgo(request)
    return res


# ***********************************  Sessionid的登录注册和退出    *****************************************************


#登录
# def login(request):
#     if request.method == "GET":
#         return render(request, 'vote/login.html')
#     else:
#         username = request.POST.get("username")
#         pwd = request.POST.get("password")
#
#         user = authenticate(request, username = username,password = pwd)
#         if user:
#             print(user)
#             lgi(request,user)
#             return redirect(reverse('vote:index'))
#         else:
#             return render(request, 'vote/login.html', {"error": "用户名或者密码错误"})

# 注册
def regist(request):
    if request.method == "POST":
        username = request.POST.get("username_regi")
        pwd = request.POST.get("password_regi")
        pwd2 = request.POST.get("password_regi_2")
        error = None
        if pwd != pwd2:
            error = "密码不正确"
            return render(request, 'vote/login.html', {"error": error})
        else:
            MyUser.objects.create_user(username= username, password=pwd, url = 'www.baidu.com')
            return redirect(reverse('vote:login'))



 # ***********************************  通过Django自带授权方法实现登录 *****************************


# 登录
# def login(request):
#     if request.method == "GET":
#         return render(request, 'vote/login.html')
#     else:
#         username=request.POST.get("username")
#         pwd = request.POST.get("password")
#         user = authenticate(request,username = username,password = pwd)
#         if user:
#             lgi(request,user)
#             return redirect(reverse('vote:index'))
#         else:
#             return render(request,'vote/login.html',{"error":"用户名或密码错误"})


# ***********************************  使用表单登录  ******************************

def login(request):
    if request.method == 'GET':
        lf =LoginForm()
        rf = RegisterForm()
        return render(request,'vote/login.html',{'lf':lf,'rf':rf})
    else:
        lf = LoginForm(request.POST)

        if lf.is_valid():
            print()
            username = lf.cleaned_data["username"]

            pwd = lf.cleaned_data["password"]

            user = authenticate(request , username = username,password=pwd)

            if user:

                lgi(request,user)
                return redirect(reverse('vote:index'))
            else:
                return render(request,'vote/login.html',{'error':"用户名或密码错误"})












