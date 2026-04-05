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

COPY . /app/

# Даем права на выполнение скрипту внутри /app
RUN chmod +x /app/entrypoint.sh

# Открываем порт (Railway сам его переопределит через переменную PORT, но для порядка пусть будет)
EXPOSE 8000

# Запускаем только через CMD
CMD ["/app/entrypoint.sh"]