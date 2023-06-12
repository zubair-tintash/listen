from django.conf import settings
from django.db import models

from songs.models import Song


class CommentsQuerySet(models.QuerySet):
    pass


class CommentsManager(models.Manager):
    def get_queryset(self):
        return CommentsQuerySet(self.model, using=self._db)


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentsManager()

    def __str__(self):
        return str(self.content)[:100]

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
