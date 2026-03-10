from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import CreateIdeaForm
from .models import Event, Idea

class EventDetailView(View):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist!")

        context = {"event": event, "idea_form": CreateIdeaForm()}

        return render(request, "../templates/event_detail.html", context=context)

class CreateEventIdeaView(LoginRequiredMixin, View):
    def post(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist!")

        form = CreateIdeaForm(request.POST)

        if form.is_valid():
            Idea.objects.create(
                owner=request.user, 
                event=event,
                title=form.cleaned_data["title"], 
                overview=form.cleaned_data["overview"]
            )

        return redirect("event-detail", event_id=event.pk)

