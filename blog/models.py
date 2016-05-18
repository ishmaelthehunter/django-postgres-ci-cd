from django.db import models


class Article(models.Model):
    title = models.CharField(blank=False, max_length=100)
    text = models.TextField(max_length=500)
    author = models.CharField(blank=False, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)


class Like(models.Model):
    article = models.ForeignKey(Article)
    created = models.DateTimeField(auto_now_add=True)
