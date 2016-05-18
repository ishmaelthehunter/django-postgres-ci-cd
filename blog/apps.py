from django.apps import AppConfig
from django.db.models.signals import post_save


class BlogAppConfig(AppConfig):
    name = 'blog'
    verbose_name = 'Blog'

    def ready(self):
        from blog import signals
        from blog import models
        post_save.connect(signals.like_post_save, sender=models.Like)
