from django.contrib.auth import get_user_model
from django.db import models

from songs.models import Song


User = get_user_model()


class NotificationsQuerySet(models.QuerySet):
    pass


class NotificationsManager(models.Manager):
    def get_queryset(self):
        return NotificationsQuerySet(self.model, using=self._db)


# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="songs")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = NotificationsManager()

    def __str__(self):
        return f"{self.timestamp}: {str(self.user)} - {str(self.song)}"

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
