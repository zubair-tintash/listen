from django.conf import settings
from django.db import models

from songs.models import Songs


class AlbumsQuerySet(models.QuerySet):
    pass


class AlbumsManager(models.Manager):
    def get_queryset(self):
        return AlbumsQuerySet(self.model, using=self._db)


# Create your models here.
class Albums(models.Model):
    name = models.TextField()
    private = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    songs = models.ForeignKey(Songs, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = AlbumsManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
