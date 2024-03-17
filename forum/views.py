# -*- coding: utf-8 -*-
# Create your views here.
# -*- coding: utf-8 -*-
# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post, PostCategory


def post_list(request):
    posts = Post.objects.all()
    ctx = {"post_list": posts}
    return render(request, "post_list.html", ctx)


def post(request, pk):
    post = Post.objects.get(pk=pk)
    ctx = {
        "name": post.title,
        "category": post.category.name,
        "entry": post.entry,
        "created_on": post.created_on,
        "updated_on": post.updated_on,
    }
    return render(request, "post_detail.html", ctx)
