#!/bin/sh

echo "🔄 Применяем миграции..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "🧹 Собираем статику..."
python manage.py collectstatic --noinput

echo "👤 Создаем суперюзера, если его нет..."
python manage.py shell <<EOF
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser(
        email='admin@example.com',
        password='1'
    )
    print("✅ Суперюзер создан: admin / 1")
else:
    print("⚠️ Суперюзер уже существует.")
EOF

echo "🚀 Запускаем Django сервер..."
exec python manage.py runserver 0.0.0.0:8000
