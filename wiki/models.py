# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        "ArticleCategory",
        on_delete=models.SET_NULL,
        null=True,
        related_name="article_category",
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = [
            "-created_on",
        ]

    def __str__(self):
        return self.title
