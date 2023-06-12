from rest_framework import serializers

from comments.api.serializers import CommentsSerializer
from comments.models import Comment
from songs.models import Song


class SongsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ["name", "artist", "tags", "timestamp", "comments"]
        read_only_fields = ["user"]

    def get_comments(self, obj):
        comments = Comment.objects.filter(song_id=obj.id)
        serializer = CommentsSerializer(comments, many=True)
        return serializer.data
