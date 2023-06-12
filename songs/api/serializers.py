from rest_framework import serializers

from albums.api.serializers import AlbumsSerializer
from albums.models import Album
from comments.api.serializers import CommentsSerializer
from comments.models import Comment
from songs.models import Song


class SongsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)
    albums = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = ["name", "artist", "tags", "albums", "timestamp", "comments"]
        read_only_fields = ["user", "albums"]

    def get_comments(self, obj):
        comments = Comment.objects.filter(song_id=obj.id)
        serializer = CommentsSerializer(comments, many=True)
        return serializer.data

    def get_albums(self, obj):
        albums = Album.objects.filter(id=obj.id)
        serializer = AlbumsSerializer(albums, many=True)
        return serializer.data
