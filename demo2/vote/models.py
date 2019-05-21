from django.db import models
from  django.contrib.auth.models import User

# Create your models here.


class VoteContent(models.Model):

    #投票内容
    votingcontent=models.CharField(max_length=30,verbose_name='投票内容')

    def __str__(self):
        return self.votingcontent

class Vote(models.Model):

    # 投票选项Mo.1
    OptionNo1=models.CharField(max_length=30,verbose_name='选项一')

    # 投票选项Mo.2
    OptionNo2 = models.CharField(max_length=30,verbose_name='选项二')

    # 投票选项Mo.1的票数
    Poll_1=models.IntegerField(max_length=50,null=True,verbose_name='选项一的票数')

    # 投票选项Mo.1的票数
    Poll_2 =models.IntegerField(null=True,verbose_name='选项二的票数')

    vo_title = models.ForeignKey('VoteContent', on_delete=models.CASCADE, verbose_name='投票名')


class MyUser(User):
    url = models.URLField(blank=True, null=True, default="http://www.baidu.com")
    class Meta():
        verbose_name = "用户"
        verbose_name_plural = verbose_name











