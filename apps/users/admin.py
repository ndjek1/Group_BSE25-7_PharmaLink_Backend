from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_superuser", "is_pharmacist", "is_patient")
    list_filter = ("is_staff", "is_superuser", "is_pharmacist", "is_patient")
    ordering = ("email",)
    search_fields = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
        ("Roles", {"fields": ("is_pharmacist", "is_patient")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_superuser", "is_pharmacist", "is_patient"),
        }),
    )

admin.site.register(User, UserAdmin)
