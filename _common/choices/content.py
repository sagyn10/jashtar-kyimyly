from django.db import models

class EventStatus(models.TextChoices):
    UPCOMING = 'upcoming', 'Предстоящие'
    PAST = 'past', 'Прошедшие'

