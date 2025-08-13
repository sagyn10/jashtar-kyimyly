from django.db import models
from django.contrib.auth.hashers import make_password

class UserProfile(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    password = models.CharField(max_length=255, verbose_name='Пароль')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ProjectApplicationLink(models.Model):
    google_form_url = models.URLField(verbose_name='Ссылка на Google Form', default='https://forms.google.com/your-form-id')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.google_form_url

    class Meta:
        verbose_name = 'Ссылка на заявку'
        verbose_name_plural = 'Ссылки на заявки'