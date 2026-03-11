from django.contrib import admin

from .models import Event, Idea, IdeaUpvote

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "organizer", "start_date", "end_date", "is_approved")

class IdeaAdmin(admin.ModelAdmin):
    list_display = ("title", "overview", "event", "owner")

class IdeaUpvoteAdmin(admin.ModelAdmin):
    list_display = ("idea", "user")

admin.site.register(Event, EventAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(IdeaUpvote, IdeaUpvoteAdmin)
