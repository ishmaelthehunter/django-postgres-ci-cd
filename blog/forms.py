from django import forms

from blog import models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'text', 'author']
