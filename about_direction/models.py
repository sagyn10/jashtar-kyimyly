import datetime

from django.db import models
from django.core.validators import FileExtensionValidator

class History(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        upload_to='experts/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg"
    )
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'История создания'
        verbose_name_plural = 'История создания'


class HistoryImage(models.Model):
    history = models.ForeignKey(
        History,
        related_name='images',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='experts/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name = 'Фотография истории создания'
        verbose_name_plural = 'Фотографии истории создания'


class Goals(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        upload_to='experts/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg"
    )
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Цели и миссия'
        verbose_name_plural = 'Цели и миссия'


class GoalImage(models.Model):
    goal = models.ForeignKey(
        Goals,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Цель"
    )
    image = models.ImageField(
        upload_to='experts/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name = 'Фотография цели'
        verbose_name_plural = 'Фотографии цели'


class Legislative(models.Model):
    law = models.CharField(max_length=155, verbose_name='Название закона')
    description = models.CharField(max_length=155, verbose_name='Описание закона', default='')
    file = models.FileField(
        upload_to='research/',
        blank=True,
        null=True,
        verbose_name='Файлы',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'word', 'excel'])],
        help_text="Загружайте файлы только в формате .pdf, .word, или .excel"
    )
    date = models.DateField(verbose_name="Дата", default=datetime.date.today)
    
    def __str__(self):
        return f'{self.law}'

    class Meta:
        verbose_name = 'Законодательная база'
        verbose_name_plural = 'Законодательная база'


class Management(models.Model):
    image = models.ImageField(
        upload_to='experts/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
        help_text="Загружайте только изображения в формате .jpeg, .png или .jpg"
    )
    full_name = models.CharField(max_length=155, verbose_name='ФИО')
    position = models.CharField(max_length=155, verbose_name='Должность')

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'
