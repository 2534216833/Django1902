from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

#首页第一个内容介绍表 需要标题和内容
class Brief(models.Model):

    title = models.CharField(max_length=50,verbose_name='标签')

    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta():
        verbose_name="介绍公司"
        verbose_name_plural = verbose_name


#首页第三个内容员工表单
class Staff(models.Model):
    name = models.CharField(max_length=20,verbose_name='名字')

    introduce = models.TextField(verbose_name='简介')

    post = models.CharField(max_length=50,verbose_name='岗位')

    class Meta():
        verbose_name="员工"
        verbose_name_plural = verbose_name


# 博客页面标签
class Tag(models.Model):

    title = models.CharField(max_length=50,verbose_name='标签')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name="标签"
        verbose_name_plural = verbose_name



# 博客页面博客内容的分类
class CateGory(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name="分类"
        verbose_name_plural = verbose_name



# 博客页面博客的所有内容
class Article(models.Model):
    #标题
    title = models.CharField(max_length=50)
    #内容
    body = models.TextField()
    #创建时间
    creat_time = models.DateTimeField(auto_now_add=True)
    #更新时间
    update_time = models.DateTimeField(auto_now=True)
    #浏览次数
    views = models.PositiveIntegerField(default=0)

    category =  models.ForeignKey(CateGory,on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag)

    auther = models.ForeignKey(User,models.CASCADE)


    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '文章'

        verbose_name_plural = verbose_name







#最后一个界面联系我们
class Contacts(models.Model):

    site = models.CharField(max_length=50,verbose_name='地址')

    phone = models.CharField(max_length=50,verbose_name='电话')

    emsil = models.CharField(max_length=50,verbose_name='邮箱')

    url = models.CharField(max_length=50,verbose_name='网站')

    # 内容
    body = models.TextField(verbose_name='内容')

    class Meta():
        verbose_name = '联系我们'

        verbose_name_plural = verbose_name



#网页开头的第一个图片内容
class Ads(models.Model):
    img = models.ImageField(upload_to='ads',verbose_name='标题的图片')
    desc = models.CharField(max_length=20,verbose_name='图片的介绍')


    class Meta():
        verbose_name = "首页第一个图片内容"
        verbose_name_plural = verbose_name



#主页的投资组合标题
class Title(models.Model):
    headline = models.CharField(max_length=20,verbose_name='图片的标题')

    class Meta():
        verbose_name = "图片的标题"
        verbose_name_plural = verbose_name


#主页的投资组合图片
class Picture(models.Model):
    img = models.ImageField(upload_to='ads',verbose_name='标题的图片')
    img_title=models.ForeignKey(Title,on_delete=models.CASCADE)


    class Meta():
        verbose_name = "投资组合图片"
        verbose_name_plural = verbose_name

#员工的头像
class Staffimage(models.Model):
    staimg = models.ImageField(upload_to='staff',verbose_name='员工头像')
    staimg_title=models.ForeignKey(Staff,on_delete=models.CASCADE)


    class Meta():
        verbose_name = "员工头像"
        verbose_name_plural = verbose_name


#首页第一个内容介绍表 需要标题和内容
class AboutUs(models.Model):

    title = models.CharField(max_length=50,verbose_name='标题')

    body = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name="关于我们"
        verbose_name_plural = verbose_name
