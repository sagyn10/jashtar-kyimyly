from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("У пользователя должен быть email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    second_name = models.CharField(max_length=255, verbose_name="Фамилия", blank=True, null=True)
    surname = models.CharField(max_length=255, verbose_name="Отчество", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class ProjectApplicationLink(models.Model):
    google_form_url = models.URLField(
        verbose_name="Ссылка на Google Form",
        default="https://forms.google.com/your-form-id"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.google_form_url

    class Meta:
        verbose_name = "Ссылка на заявку"
        verbose_name_plural = "Ссылки на заявки"