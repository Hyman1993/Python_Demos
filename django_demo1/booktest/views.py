from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
# HttpRequest
def index(request):
    # HttpResponse
    # context = {'title': 'django 首页', 'list': range(10)}
    # 跳转到页面模板并传递参数
    # return render(request, 'booktest/index.html',context)
    list = BookInfo.objects.all()
    context = {'booklist': list}
    return render(request, 'booktest/index2.html', context)


def detail(request, id):
    list = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {'herolist': list}
    return render(request, 'booktest/detail.html', context)
