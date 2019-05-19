
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from  .models import VoteContent,Vote

# Create your views here.

# 查看投票信息
def index(request):
    allvote=VoteContent.objects.all()
    # return HttpResponse("list列表页")
    temp1=loader.get_template('vote/index.html')
    result=temp1.render({'allvote':allvote})
    return HttpResponse(result)


# 投票选择界面
def VotingPage(request,id):

    voting = VoteContent.objects.get(pk=id)

    if request.method == "GET":
        temp2 = loader.get_template('vote/votingpage.html')
        result = temp2.render({'voting': voting})
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



def VotingResult(request,id):
    pass
    result=Vote.objects.get(pk=id)
    print(result)
    return HttpResponse("这是投票结果页")





















