from django.contrib.auth import get_user_model
from rest_framework import serializers

from notifications.models import Notification
from songs.api.serializers import SongsSerializer
from songs.models import Song


User = get_user_model()


class UserListingField(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, user):
        return user.username


class NotificationsSerializer(serializers.ModelSerializer):
    user = UserListingField(read_only=True)
    song = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Notification
        fields = ["user", "song"]
        read_only_fields = ["user", "song"]

    def get_user(self, obj):
        return User.objects.filter(id=obj.id).username

    def get_song(self, obj):
        songs = Song.objects.filter(id=obj.id)
        serializer = SongsSerializer(songs, many=True)
        return serializer.data[0]["name"]
