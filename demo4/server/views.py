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
    # staffimg =Staffimage.objects.all()
    # for i in articles:
    #     print(i.title)
    return render(request,'index.html',locals())


def detail(request):
    return render(request,'detail.html')