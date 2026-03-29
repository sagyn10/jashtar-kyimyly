from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, **extra_fields):
        if not email:
            raise ValueError("У пользователя должен быть email")
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, full_name, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    full_name = models.CharField(max_length=255, verbose_name="ФИО", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    second_name = models.CharField(max_length=255, verbose_name="Фамилия", blank=True, null=True)
    surname = models.CharField(max_length=255, verbose_name="Отчество", blank=True, null=True)
    is_active = models.BooleanField(default=False)  # ⬅️ теперь новый пользователь неактивен
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(null=True, blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.email



class UserCabinet(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="cabinet")
    projects = models.ManyToManyField('content.Projects', related_name='users', blank=True)
    telegram_channel = models.URLField(blank=True, null=True, verbose_name="Ссылка на Telegram-канал")
    google_form_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на Google Form")
    education_materials = models.ManyToManyField(
        'content.EducationMaterial', blank=True, related_name="cabinets", verbose_name="Обучающие материалы"
    )

    def __str__(self):
        return f"Кабинет {self.user.email}"
    
    class Meta:
        verbose_name = "Кабинет пользователя"
        verbose_name_plural = "Кабинеты пользователей"
