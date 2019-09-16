from django.conf.urls import url

from booktest.views import index, detail

urlpatterns = [
    url('^$', index),
    url('^(\d+)/$', detail),
]
