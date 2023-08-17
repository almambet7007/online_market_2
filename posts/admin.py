from django.contrib import admin

from posts.models import Post, Hashtag

admin.site.register(Post)    #registration
admin.site.register(Hashtag)
