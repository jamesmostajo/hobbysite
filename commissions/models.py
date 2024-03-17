# -*- coding: utf-8 -*-
# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "created_on",
        ]


class Comment(models.Model):
    commission = models.ForeignKey(
        "Commission",
        on_delete=models.CASCADE,
        related_name="commissions",
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.commission.title} on {self.created_on}"

    def get_absolute_url(self):
        return reverse("commissions:comment_detail", args=[str(self.pk)])

    class Meta:
        ordering = [
            "-created_on",
        ]
