RUN apt-get update && apt-get install -y \
    gettext \
    libpq-dev \
    curl \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /jashtar-kyimyly/

WORKDIR /jashtar-kyimyly

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Сборка статики
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "-w", "4", "-b", "0.0.0.0:8000"]