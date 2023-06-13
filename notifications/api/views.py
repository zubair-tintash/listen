from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from .serializers import NotificationsSerializer
from notifications.models import Notification


class NotificationsAPIListView(generics.ListAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NotificationsSerializer
    search_fields = ("name", "song")
    queryset = Notification.objects.all()
    lookup_field = "id"


class NotificationsAPIView(mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NotificationsSerializer
    passed_id = None
    queryset = Notification.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
