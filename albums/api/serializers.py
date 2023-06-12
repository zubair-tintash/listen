from rest_framework import serializers

from albums.models import Album


class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["name", "private", "timestamp", "songs"]
        read_only_fields = ["user"]
