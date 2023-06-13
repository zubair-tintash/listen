from rest_framework import serializers

from notifications.models import Notification


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["user", "song"]
        read_only_fields = ["user", "song"]
