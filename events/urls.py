from django.urls import path

from .views import EventDetailView, CreateEventIdeaView

urlpatterns = [
    path("<int:event_id>", EventDetailView.as_view(), name="event-detail"),
    path("<int:event_id>/ideas/", CreateEventIdeaView.as_view(), name="create-idea"),
]
