from django.contrib.auth import get_user_model
from django.db import models

from songs.models import Song


User = get_user_model()


class CommentsQuerySet(models.QuerySet):
    pass


class CommentsManager(models.Manager):
    def get_queryset(self):
        return CommentsQuerySet(self.model, using=self._db)


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="comments")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentsManager()

    def __str__(self):
        return f"{self.song.name} - {self.name}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
