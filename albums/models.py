from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class AlbumsQuerySet(models.QuerySet):
    pass


class AlbumsManager(models.Manager):
    def get_queryset(self):
        return AlbumsQuerySet(self.model, using=self._db)


# Create your models here.
class Album(models.Model):
    name = models.TextField()
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = AlbumsManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
