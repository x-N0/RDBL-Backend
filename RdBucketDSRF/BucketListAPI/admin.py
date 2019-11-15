from django.contrib import admin
from .models import *
from django_comments.models import Comment
# Register your models here.
admin.site.register(BucketList)
admin.site.register(CustomComment)
