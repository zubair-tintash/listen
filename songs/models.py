from django.conf import settings
from django.db import models


class SongsQuerySet(models.QuerySet):
    pass


class SongsManager(models.Manager):
    def get_queryset(self):
        return SongsQuerySet(self.model, using=self._db)


# Create your models here.
class Song(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField()
    artist = models.TextField()
    tags = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = SongsManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
