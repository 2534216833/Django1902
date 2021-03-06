from django.db import models
from blogs.models import Article
from datetime import datetime


class Comment(models.Model):
    username = models.CharField(max_length=30)

    email = models.EmailField(blank=True,null= True)

    url = models.URLField(blank=True,null=True)

    content = models.CharField(max_length=500)

    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    create_time = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta():
        verbose_name = '评价'

        verbose_name_plural = verbose_name



