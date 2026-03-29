import random
from django.core.mail import send_mail
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.db.models.signals import post_save

from .models import UserProfile, UserCabinet


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Генерация случайного 4-значного кода
    reset_code = random.randint(1000, 9999)

    # Сохраняем код в поле key токена
    reset_password_token.key = str(reset_code)
    reset_password_token.save()

    # Текст письма
    email_message = f"Ваш код для сброса пароля: {reset_code}"

    # Отправляем email пользователю
    send_mail(
        subject="Сброс пароля",
        message=email_message,
        from_email="noreply@myproject.local",
        recipient_list=[reset_password_token.user.email],
        fail_silently=False,
    )


@receiver(post_save, sender=UserProfile)
def create_user_cabinet(sender, instance, created, **kwargs):
    """Автоматически создаём личный кабинет для каждого нового пользователя"""
    if created:
        UserCabinet.objects.create(user=instance)
