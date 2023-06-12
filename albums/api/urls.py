from django.conf.urls import url

from .views import AlbumsAPIDetailView
from .views import AlbumsAPIView


urlpatterns = [
    url(r"^$", AlbumsAPIView.as_view()),
    url(r"^(?P<id>\d+)/$", AlbumsAPIDetailView.as_view()),
]
