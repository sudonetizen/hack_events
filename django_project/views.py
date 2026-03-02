from django.shortcuts import render
from django.utils import timezone

from events.models import Event

def home_page(request):
    now = timezone.now()
    active_hack_events = Event.objects.filter(is_approved=True, start_date__lt=now, end_date__gt=now)
    coming_hack_events = Event.objects.filter(is_approved=True, start_date__gt=now)
    past_hack_events = Event.objects.filter(is_approved=True, end_date__lt=now)

    context = {
        "past_hack_events": past_hack_events,
        "active_hack_events": active_hack_events,
        "coming_hack_events": coming_hack_events,
    }

    return render(request, "home.html", context) 
