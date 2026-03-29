from datetime import datetime, date
from enum import StrEnum
from io import BytesIO

from django.core.files.base import ContentFile
from django.db import models
from django.core.validators import FileExtensionValidator, URLValidator
from django.core.exceptions import ValidationError as ORMValidationError
from PIL import Image
from jsonschema.exceptions import ValidationError as JSONValidationError

from _common.choices.content import EventStatus

def current_time():
    return datetime.now().time()


class Events(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название мероприятия')
    description = models.TextField(verbose_name='Описание мероприятия')
    # slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время", default=current_time)
    event_status = models.CharField(
        max_length=255,
        verbose_name='Статус мероприятия',
        choices=EventStatus.choices
    )
    place = models.CharField(max_length=155, verbose_name='Местоположение мероприятия', default='Улица, дом')

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
    # slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)
    goals = models.TextField(verbose_name='Цели проекта', blank=True, null=True)
    tasks = models.TextField(verbose_name='Задачи проекта', blank=True, null=True)
    image = models.ImageField(
        upload_to='project_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Главная фотография",
        null=True
    )
    
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

    def __str__(self) -> str:
        return f'{self.title}'

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
    title = models.CharField(max_length=125, null=True, verbose_name='Название изображения')
    date = models.DateField(null=True, default=date.today, verbose_name='Дата изображений')

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
    short_description = models.CharField("Короткое описание направления", max_length=100, blank=True, null=False)
    description = models.TextField('Описание деятельности', blank=False, null=False)

    telegram_link = models.CharField(max_length=255, default='https://example.com', blank=True, null=False)
    instagram_link = models.CharField(max_length=255, default='https://example.com', blank=True, null=False)

    image = models.ImageField(
        upload_to='activity-directions/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg или .jpeg"
    )

    class Meta:
        verbose_name = 'Направление деятельности'
        verbose_name_plural = 'Направление деятельности'


class Departments(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название отделения')
    description = models.TextField(verbose_name='Описание') #RichText
    address = models.CharField(max_length=99, verbose_name='Адрес отделения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Региональные отделения'
        verbose_name_plural = 'Региональные отделения'


# class DepartmentImage(models.Model):
#     department = models.ForeignKey(
#         Departments,
#         related_name='images',
#         on_delete=models.CASCADE,
#         verbose_name="Отделение"
#     )
#     image = models.ImageField(
#         upload_to='department_photos/',
#         validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
#         verbose_name="Фотография"
#     )

#     def save(self, *args, **kwargs):
#         if self.department.images.count() >= 5: # type: ignore
#             raise JSONValidationError("Нельзя добавить больше 5 изображений для отделения.")
#         if self.image:
#             img = Image.open(self.image)
#             img = img.convert('RGB')
#             output = BytesIO()
#             img.save(output, format='JPEG', quality=75)
#             output.seek(0)
#             self.image.save(self.image.name, ContentFile(output.read()), save=False)
#         super().save(*args, **kwargs)

#     class Meta:
#         verbose_name = 'Фотография отделения'
#         verbose_name_plural = 'Фотографии отделения'

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
    # slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Employee(models.Model):
    name = models.CharField('ФИО сотрудника', max_length=255)
    position = models.CharField('Позиция сотрудника', max_length=100)

    image = models.ImageField(
        upload_to='employees/',
        verbose_name="Фото сотрудника",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg или .jpeg",
        blank=True,
    )

    department = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE,
        verbose_name='Отделение',
        related_name='employees',
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class AttachmentTypeEnum(StrEnum):
    DOCUMENT = 'document'
    VIDEO = 'video'
    LINK = 'link'

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        return [(key.value, key.name) for key in cls]


class EducationMaterial(models.Model):
    title = models.CharField(max_length=155, null=False, blank=False, verbose_name="Название")
    attachment_type = models.CharField(
        max_length=20,
        choices=AttachmentTypeEnum.choices(), 
        default=AttachmentTypeEnum.DOCUMENT.value,
        verbose_name="Тип вложения",
    )
    attachment = models.FileField(
        upload_to='education_materials/',
        verbose_name="Вложение",
        blank=True,
        null=True,
        help_text="Загружайте документы (.pdf, .docx, .txt) или видео (.mp4, .mov, .avi)",
    )
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        validators=[URLValidator()],
        help_text="Если тип вложения link, вставьте ссылку сюда",
        verbose_name="Ссылка",
    )

    def clean(self):
        """Валидация: attachment или link должны соответствовать типу"""
        if self.attachment_type in (
            AttachmentTypeEnum.VIDEO.value,
            AttachmentTypeEnum.DOCUMENT.value,
        ):
            if not self.attachment:
                raise ORMValidationError('Для типа document или video нужно загрузить файл.')
            
            if self.attachment_type == AttachmentTypeEnum.VIDEO.value:
                allowed = ['mp4', 'mov', 'avi']
                extension = self.attachment.name.split('.')[-1].lower()
                if extension not in allowed:
                    raise ORMValidationError(f"Файл должен быть одного из форматов: [{', '.join(allowed)}]")
            
        elif self.attachment_type == AttachmentTypeEnum.LINK.value:
            if not self.link:
                raise ORMValidationError("Для типа LINK нужно указать ссылку.")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Обучающий материал"
        verbose_name_plural = "Обучающие материалы"


class Course(models.Model):

    title = models.CharField(max_length=155, null=False, blank=False, verbose_name="Название")
    image = models.ImageField(
        upload_to='courses/',
        verbose_name="Фото",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg или .jpeg",
    )
    description = models.CharField("Описание", max_length=155, blank=True, null=False)

    link = models.URLField(
        max_length=500,
        validators=[URLValidator()],
        verbose_name="Ссылка",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
