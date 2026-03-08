from django.urls import path

from .views import EventDetailView

urlpatterns = [
    path("<int:event_id>", EventDetailView.as_view(), name="event-detail"),
]
