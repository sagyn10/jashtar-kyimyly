FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Сборка статики
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Копируем entrypoint и делаем исполняемым
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
