# -*- coding: utf-8 -*-
# Create your views here.
# -*- coding: utf-8 -*-
# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Comment, Commission


def comment_list(request):
    comments = Comment.objects.all()
    ctx = {"comment_list": comments}
    return render(request, "comment_list.html", ctx)


def comment_detail(request, pk):
    comment = Comment.objects.get(pk=pk)
    ctx = {
        "name": comment.commission.title,
        "entry": comment.entry,
        "created_on": comment.created_on,
        "updated_on": comment.updated_on,
    }
    return render(request, "comment_detail.html", ctx)
