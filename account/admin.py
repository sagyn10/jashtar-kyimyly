from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, ProjectApplicationLink


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = ("email", "name", 'second_name', 'surname', "is_staff", "is_active", "last_login")
    list_filter = ("is_staff", "is_active")
    ordering = ("email",)
    search_fields = ("email", "full_name")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "password1", "password2", "is_staff", "is_active"),
        }),
    )


@admin.register(ProjectApplicationLink)
class ProjectApplicationLinkAdmin(admin.ModelAdmin):
    list_display = ("google_form_url", "updated_at")