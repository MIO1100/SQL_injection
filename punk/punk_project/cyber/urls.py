from django.conf.urls import  url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^art/$', views.art, name='art'),
    url(r'^info/$', views.info, name='info'),
    url(r'^search/$', views.search, name='search'),

    url(r'^search_proc/$', views.search_proc, name='search_proc'),
]
