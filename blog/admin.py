from django.contrib import admin
from blog.models import Post, Tag, Comment


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post', 'author']
    list_display = ['author', 'post', 'published_at']


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['tags', 'author', 'likes']


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
