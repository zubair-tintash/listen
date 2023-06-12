from django.conf.urls import url

from .views import CommentsAPIDetailView
from .views import CommentsAPIView


urlpatterns = [
    url(r"^$", CommentsAPIView.as_view()),
    url(r"^(?P<id>\d+)/$", CommentsAPIDetailView.as_view()),
]
