from rest_framework import serializers

from .models import Album


class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["name", "private", "user"]
