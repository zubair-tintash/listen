from django.contrib.auth import get_user_model
from rest_framework import serializers

from albums.api.serializers import AlbumsSerializer
from albums.models import Album
from comments.api.serializers import CommentsSerializer
from comments.models import Comment
from songs.models import Song


User = get_user_model()


class UserListingField(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, user):
        return user.username


class SongsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)
    albums = serializers.SerializerMethodField(read_only=True)
    likes = UserListingField(many=True, queryset=User.objects.all())
    favorites = UserListingField(many=True, queryset=User.objects.all())

    class Meta:
        model = Song
        fields = [
            "name",
            "artist",
            "tags",
            "likes",
            "favorites",
            "albums",
            "timestamp",
            "comments",
        ]

    def get_comments(self, obj):
        comments = Comment.objects.filter(song_id=obj.id)
        serializer = CommentsSerializer(comments, many=True)
        return serializer.data

    def get_albums(self, obj):
        albums = Album.objects.filter(id=obj.id)
        serializer = AlbumsSerializer(albums, many=True)
        return serializer.data

    def get_likes(self, obj):
        users = User.objects.filter(username__in=obj.likes.all())
        return [u.username for u in users]

    def get_favorites(self, obj):
        users = User.objects.filter(username__in=obj.favorites.all())
        return [u.username for u in users]
