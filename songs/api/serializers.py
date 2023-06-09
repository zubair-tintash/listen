from rest_framework import serializers

from songs.models import Songs


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ["name", "artist" "tags"]
        read_only_fields = ["user"]
