from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.articles_list', name='articles-list'),
    url(r'^new$', 'blog.views.new_article', name='articles-new'),
    url(r'^like/(?P<article_id>\d+)$', 'blog.views.article_like',
        name='articles-like'),
)
