from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.core.validators import FileExtensionValidator, URLValidator
from jsonschema.exceptions import ValidationError

from _common.choices.content import EventStatus


class Events(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название мероприятия')
    description = models.TextField(verbose_name='Описание мероприятия')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    date = models.DateField(verbose_name="Дата")
    event_status = models.CharField(
        max_length=255,
        verbose_name='Статус мероприятия',
        choices=EventStatus.choices
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class EventImage(models.Model):
    event = models.ForeignKey(
        Events,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Мероприятие"
    )
    image = models.ImageField(
        upload_to='event_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name = 'Фотография мероприятия'
        verbose_name_plural = 'Фотографии мероприятия'


class Projects(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectsImage(models.Model):
    project = models.ForeignKey(
        Projects,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Проект"
    )
    image = models.ImageField(
        upload_to='project_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name = 'Фотография проекта'
        verbose_name_plural = 'Фотографии проекта'


class Gallery(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название')
    date = models.DateField(verbose_name="Дата")

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class GalleryImage(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Галерея"
    )
    image = models.ImageField(
        upload_to='gallery_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img = img.convert('RGB')

            output = BytesIO()
            img.save(output, format='JPEG', quality=75)
            output.seek(0)

            self.image.save(self.image.name, ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотография галереи'
        verbose_name_plural = 'Фотографии галереи'


class VideoArchive(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название видеоматериала')
    video_url = models.URLField(
        verbose_name='Ссылка на видеоматериал',
        validators=[
            URLValidator(
                schemes=['https'],
                regex=r'^https?://(www\.)?(youtube\.com|youtu\.be)/.+$'
                )
            ]
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видеоархив'
        verbose_name_plural = 'Видеоархивы'


class ActivityDirection(models.Model):
    title = models.CharField("Название направления", max_length=255,  blank=False,null=False)
    description = models.TextField('Описание деятельности', blank=False, null=False)

    class Meta:
        verbose_name = 'Направление деятельности'
        verbose_name_plural = 'Направление деятельности'


class Departments(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название отделения')
    description = models.TextField(verbose_name='Описание') #RichText
    address = models.CharField(max_length=99, verbose_name='Адрес отделения')
    image = models.ImageField(
        upload_to='experts/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg или .jpeg"
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Региональные отделения'
        verbose_name_plural = 'Региональные отделения'


class DepartmentImage(models.Model):
    department = models.ForeignKey(
        Departments,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Отделение"
    )
    image = models.ImageField(
        upload_to='department_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )

    def save(self, *args, **kwargs):
        if self.department.images.count() >= 5:
            raise ValidationError("Нельзя добавить больше 5 изображений для отделения.")
        if self.image:
            img = Image.open(self.image)
            img = img.convert('RGB')
            output = BytesIO()
            img.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.image.save(self.image.name, ContentFile(output.read()), save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотография отделения'
        verbose_name_plural = 'Фотографии отделения'

class Results(models.Model):
    title = models.TextField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание') #RichText

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Результаты'
        verbose_name_plural = 'Результаты'


class News(models.Model):
    image = models.ImageField(
        upload_to='experts/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg или .jpeg"
    )
    title = models.CharField(max_length=99, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    slug = models.SlugField(max_length=255, unique=True, blank=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'