"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase

from .models import Article

# TODO: Configure your database in settings.py and sync before running tests.

class ArticleModelTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        django.setup()
        super(ArticleModelTest, cls).setUpClass()

    # проверка заполнения пустого поля "дата" и добавления тегов
    def test_fill_date_if_empty(self):
        article = Article(title = "test", articleContent = "test")
        article.save()
        article.tags.add("red", "green", "fruit")
        self.assertNotEqual(article.pub_date, None)
        self.assertEqual(set([tag.name for tag in article.tags.all()]), {"green", "fruit", "red"})