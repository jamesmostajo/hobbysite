# -*- coding: utf-8 -*-
# Register your models here.
# -*- coding: utf-8 -*-
# Register your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin

from .models import Post, PostCategory


class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory


class PostAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
