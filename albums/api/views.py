from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from .serializers import AlbumsSerializer
from albums.models import Album


class AlbumsAPIDetailView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AlbumsSerializer
    queryset = Album.objects.all()
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(updated_by_user=self.request.user)


class AlbumsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AlbumsSerializer
    passed_id = None
    search_fields = ("name", "private", "user")
    queryset = Album.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
