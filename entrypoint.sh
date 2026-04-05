#!/bin/bash

# Остановить выполнение, если какая-то команда вернула ошибку
set -e

export DJANGO_SETTINGS_MODULE=config.settings.settings

echo "🔄 Применяем миграции..."
# Мы НЕ делаем makemigrations здесь, только применяем готовые
python manage.py migrate --noinput

echo "🧹 Собираем статику..."
python manage.py collectstatic --noinput

echo "👤 Проверяем суперюзера..."
python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('SUPERUSER_USERNAME')
email = os.environ.get('SUPERUSER_EMAIL')
password = os.environ.get('SUPERUSER_PASSWORD')

# Проверяем по email или по username (зависит от твоей модели)
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"✅ Суперюзер {username} успешно создан!")
else:
    print("⚠️ Суперюзер уже существует.")
EOF

echo "🚀 Запускаем Gunicorn..."
# Railway сам подставляет переменную PORT, поэтому используем её
exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}