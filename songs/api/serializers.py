from rest_framework import serializers

from songs.models import Song


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["name", "artist", "tags"]
        read_only_fields = ["user"]
