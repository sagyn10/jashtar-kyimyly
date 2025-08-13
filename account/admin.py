from django.contrib import admin
from .models import UserProfile, ProjectApplicationLink


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')
    search_fields = ('full_name', 'email')
    list_filter = ('email',)
    ordering = ('id',)


@admin.register(ProjectApplicationLink)
class ProjectApplicationLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'google_form_url')
    search_fields = ('google_form_url',)
