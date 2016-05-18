from django.test import TestCase
from blog import models


class ModelsCase(TestCase):
    def setUp(self):
        self.article = models.Article.objects.create(
            title='New article', text='Demo text', author='42')

    def test_like_increment(self):
        """
        Test that creating a like, correctly increments the counter of the
        article.
        """
        models.Like.objects.create(article=self.article)
        self.article.refresh_from_db()
        self.assertEqual(self.article.like_count, 1)
