# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Article, ArticleCategory


def article_list(request):
    articles = Article.objects.all()
    ctx = {"articles_list": articles}
    return render(request, "article_list.html", ctx)


def article(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {
        "name": article.name,
        "category": article.article_category.name,
        "entry": article.entry,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
    }
    return render(request, "article_detail.html", ctx)
