from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# HttpRequest
def index(request):
    # HttpResponse
    context = {'title': 'django 首页', 'list': range(10)}
    # 跳转到页面模板并传递参数
    return render(request, 'booktest/index.html',context)
