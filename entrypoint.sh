#!/bin/bash

export DJANGO_SETTINGS_MODULE=config.settings.settings
echo "🔄 Применяем миграции..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "🧹 Собираем статику..."
python manage.py collectstatic --noinput

echo "👤 Создаем суперюзера, если его нет..."
python manage.py shell <<EOF
import django
django.setup()
from django.conf import settings
from account.models import UserProfile

if not UserProfile.objects.filter(is_superuser=True).exists():
    UserProfile.objects.create_superuser(
        email=settings.SUPERUSER_EMAIL,
        full_name=settings.SUPERUSER_NAME,
        password=settings.SUPERUSER_PASSWORD,
        is_active=True
    )
    print("✅ Суперюзер создан: admin / 1")
else:
    print("⚠️ Суперюзер уже существует.")
EOF

echo "🚀 Запускаем Django сервер..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
