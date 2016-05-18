from django.db.models import F


def like_post_save(sender, instance, created, **kwargs):
    if created:
        article = instance.article
        article.like_count = F('like_count') + 1
        article.save()
