from django.conf.urls import url

from booktest.views import index

urlpatterns = [
    url('index/', index),
]
