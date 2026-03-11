from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError 
from django.db.models import Exists, OuterRef
from django.views import View

from .forms import CreateIdeaForm
from .models import Event, Idea, IdeaUpvote

class EventDetailView(View):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist!")

        ideas = event.ideas.annotate(
            is_liked=Exists(
                IdeaUpvote.objects.filter(user=request.user, idea=OuterRef("pk"))
            )
        )
        context = {"event": event, "idea_form": CreateIdeaForm(), "ideas": ideas}

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

class UpvoteIdeaView(LoginRequiredMixin, View):
    def post(self, request, event_id, idea_id):
        try:
            idea = Idea.objects.get(pk=idea_id, event__id=event_id)
        except Idea.DoesNotExist:
            return HttpResponse("Idea does not exist")

        try: 
            IdeaUpvote.objects.create(idea=idea, user=request.user)
        except IntegrityError:
            return HttpResponse("one user can upvote any idea once only!")

        return redirect("event-detail", event_id=event_id)
