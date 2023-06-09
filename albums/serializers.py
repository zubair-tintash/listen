from rest_framework import serializers

from .models import Albums


class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ["name", "private", "user"]
