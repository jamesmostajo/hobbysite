# -*- coding: utf-8 -*-
# Create your models here.
# -*- coding: utf-8 -*-
# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        "PostCategory",
        on_delete=models.SET_NULL,
        null=True,
        related_name="post_category",
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("forum:post_detail", args=[str(self.pk)])

    class Meta:
        ordering = [
            "-created_on",
        ]
