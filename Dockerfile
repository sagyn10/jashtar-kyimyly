FROM python:3.12-slim

# Установка системных зависимостей (для psycopg2, Pillow и т.п.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Настройка рабочей директории
WORKDIR /app

# Установка зависимостей проекта
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение
COPY . /app/

# Копируем entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Открываем порт
EXPOSE 8000

# Используем entrypoint для запуска миграций и gunicorn
ENTRYPOINT ["/entrypoint.sh"]
