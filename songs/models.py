from django.contrib.auth import get_user_model
from django.db import models

from albums.models import Album


User = get_user_model()


class SongsQuerySet(models.QuerySet):
    pass


class SongsManager(models.Manager):
    def get_queryset(self):
        return SongsQuerySet(self.model, using=self._db)


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    tags = models.TextField(null=True)
    albums = models.ManyToManyField(Album, related_name="songs")
    likes = models.ManyToManyField(User, related_name="likes")
    favorites = models.ManyToManyField(User, related_name="favorites")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = SongsManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
