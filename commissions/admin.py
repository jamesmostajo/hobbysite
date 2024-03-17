# -*- coding: utf-8 -*-
# Register your models here.
# -*- coding: utf-8 -*-
# Register your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin

from .models import Comment, Commission


class CommissionAdmin(admin.ModelAdmin):
    model = Commission


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
