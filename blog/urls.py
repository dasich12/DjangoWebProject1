# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.ArticlesView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.ArticleDetailView.as_view(),
        name='article_detail'),
    url(r'^(?P<article_id>[0-9]+)/comment/$', views.add_comment,
        name='add_comment'),
    url(r'^tag/(?P<tag>[\w ]+)$', views.tags, name='article_tags')
]
