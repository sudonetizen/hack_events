from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
   ordering = ("pk",)
   list_display = ("email", "first_name", "last_name", "is_staff", "is_active")


admin.site.register(CustomUser, CustomUserAdmin)
