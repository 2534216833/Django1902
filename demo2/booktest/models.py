from django.db import models

# Create your models here.
class BookInfo(models.Model):


    title=models.CharField(max_length=30,verbose_name='书名')

    pub_date=models.DateTimeField(auto_now_add=True,verbose_name="出版时间")

    def __str__(self):
        return self.title




GENDER=( ('1',"男"),('2',"女") )
class HeroInfo(models.Model):
    name=models.CharField(max_length=30,verbose_name="角色名")

    # gender=models.BooleanField(default=True,verbose_name='性别')
    gender=models.CharField(max_length=10,choices=GENDER,verbose_name="性别")

    skill=models.CharField(max_length=50,null=True,verbose_name="绝招")

    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='书')

    def __str__(self):
        return self.name

