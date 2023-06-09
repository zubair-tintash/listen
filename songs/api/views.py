import json

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

from .serializers import SongsSerializer
from songs.models import Songs

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404


def is_json(json_data):
    try:
        json.loads(json_data)
        return True
    except ValueError:
        return False


# Create your views here.
# class SongsListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Songs.objects.all()
#         serializer = SongsSerializer(qs, many=True)
#         return Response(serializer)
#
#     def post(self, request, format=None):
#         qs = Songs.objects.all()
#         serializer = SongsSerializer(qs, many=True)
#         return Response(serializer)


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

    def get_queryset(self):
        request = self.request
        qs = Songs.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('id', None) or self.passed_id
    #     queryset = self.get_queryset()
    #     obj = None
    #     if passed_id is not None:
    #         obj = get_object_or_404(queryset, id=passed_id)
    #         self.check_object_permissions(request, obj)
    #     return obj
    #
    # def get(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     if passed_id is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def put(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     return self.partial_update(request, *args, **kwargs)


# class SongsCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Songs.objects.all()
#     serializer_class = SongsSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class SongsDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Songs.objects.all()
#     serializer_class = SongsSerializer
#     lookup_field = 'id'
#
#     def get_object(self, *args, **kwargs):
#         kwargs = self.kwargs
#         kw_id = kwargs.get('id')
#         return Songs.objects.get(id=kw_id)
#
#
# class SongsUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Songs.objects.all()
#     serializer_class = SongsSerializer
