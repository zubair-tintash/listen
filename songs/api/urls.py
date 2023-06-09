from django.conf.urls import url

from .views import SongsAPIDetailView
from .views import SongsAPIView


urlpatterns = [
    url(r"^$", SongsAPIView.as_view()),
    url(r"^(?P<id>\d+)/$", SongsAPIDetailView.as_view()),
]
