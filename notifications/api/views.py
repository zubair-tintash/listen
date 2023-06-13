from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from .serializers import NotificationsSerializer
from notifications.models import Notification


class NotificationsAPIView(
    mixins.CreateModelMixin, generics.ListAPIView, generics.RetrieveAPIView
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NotificationsSerializer
    passed_id = None
    search_fields = ("name", "song")
    queryset = Notification.objects.all()
    lookup_field = "id"

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(name=self.request.user.username)
