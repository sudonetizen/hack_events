from django.contrib import admin
from django.urls import path, include

from .views import home_page

urlpatterns = [
    path("", home_page, name="home"), 
    path("accounts/", include("accounts.urls")),
    path("events/", include("events.urls")),
    path("admin/", admin.site.urls),
]
