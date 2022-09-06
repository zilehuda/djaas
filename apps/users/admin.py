from django.contrib import admin

from apps.users.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
    )


admin.site.register(User, CustomUserAdmin)
