from django.contrib import admin

from posts.models import Post, Hashtag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'rate', 'created_date','modified_date')

admin.site.register(Hashtag)
