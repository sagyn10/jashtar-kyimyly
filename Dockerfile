FROM python:3.10-slim

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

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
