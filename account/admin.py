from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_rest_passwordreset.models import ResetPasswordToken
from .models import UserProfile


# Убираем модель ResetPasswordToken из админки, она не нужна
try:
    admin.site.unregister(ResetPasswordToken)
except admin.sites.NotRegistered:
    pass


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    model = UserProfile

    # что будет видно в списке пользователей
    list_display = ("email", "full_name", "is_staff", "is_active", "last_login")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "full_name")
    ordering = ("email",)

    # как редактируется пользователь
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Личная информация", {"fields": ("full_name", "name", "second_name", "surname")}),
        ("Права доступа", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    # как выглядит форма добавления нового пользователя
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "password1", "password2", "is_staff", "is_active"),
        }),
    )


# Чтобы в админке писалось красиво (в models.py у UserProfile)
UserProfile._meta.verbose_name = "Пользователь"
UserProfile._meta.verbose_name_plural = "Пользователи"