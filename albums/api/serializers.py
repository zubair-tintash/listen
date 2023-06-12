from rest_framework import serializers

from albums.models import Album
from songs.api.serializers import SongsSerializer
from songs.models import Song


class AlbumsSerializer(serializers.ModelSerializer):
    # songs = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ["name", "private", "timestamp", "songs"]
        read_only_fields = ["user"]

    # def get_songs(self, obj):
    #     songs = Song.objects.filter(id=obj.id)
    #     serializer = SongsSerializer(songs, many=True)
    #     return serializer.data
