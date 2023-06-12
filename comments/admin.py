from django.contrib import admin

from .models import Comment

admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "content", "song", "timestamp")
    list_filter = ("timestamp", "updated")
    search_fields = ("name", "content", "song")
