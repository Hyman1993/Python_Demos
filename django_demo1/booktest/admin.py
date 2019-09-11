import django.contrib
from .models import *
# Register your models here.

from booktest.models import BookInfo, HeroInfo

class BookInfoAdmin(django.contrib.admin.ModelAdmin):
    list_display = ['id','title','pub_date']

class HeroInfoAdmin(django.contrib.admin.ModelAdmin):
    list_display = ['id','name','content','gender','book']

django.contrib.admin.site.register(BookInfo,BookInfoAdmin)
django.contrib.admin.site.register(HeroInfo,HeroInfoAdmin)
