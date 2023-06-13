from django.conf.urls import url

from .views import NotificationsAPIListView


urlpatterns = [
    url(r"^$", NotificationsAPIListView.as_view()),
]
