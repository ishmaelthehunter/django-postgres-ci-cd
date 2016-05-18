from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from blog import forms
from blog import models


def articles_list(request):
    context = {
        'articles': models.Article.objects.order_by('-created').all(),
    }
    return render(request, 'blog/articles_list.html', context=context)


def article_like(request, article_id):
    article = get_object_or_404(models.Article, pk=article_id)
    models.Like.objects.create(article=article)
    return redirect('/')


def new_article(request):
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('/')
    else:
        form = forms.ArticleForm()
    return render(request, 'blog/new_article.html', {'form': form})
