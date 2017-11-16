
from django.conf.urls import url,include
from django.contrib import admin
from .views import getform,newmessage

urlpatterns = [
    url(r'^$', getform),
    url(r'^newmessage/$', newmessage),
]
