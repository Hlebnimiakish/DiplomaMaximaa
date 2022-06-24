from django.contrib import admin
from tropic_starter.models import Post, Comment, TSUser

admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(TSUser)