import json

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from .serializers import SongsSerializer
from songs.models import Songs


def is_json(json_data):
    try:
        json.loads(json_data)
        return True
    except ValueError:
        return False


class SongsAPIDetailView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SongsSerializer
    queryset = Songs.objects.all()
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(updated_by_user=self.request.user)


class SongsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SongsSerializer
    passed_id = None
    search_fields = ("name", "tags")
    queryset = Songs.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
