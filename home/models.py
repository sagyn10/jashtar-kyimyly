from django.db import models
from django.core.validators import FileExtensionValidator



class Banner(models.Model):
    image = models.FileField(
        upload_to='banners/',
        verbose_name="Изображение (SVG)",
        validators=[FileExtensionValidator(allowed_extensions=['svg'])],
        help_text="Загружайте только изображения в формате .svg"
    )
    description = models.CharField(max_length=255, verbose_name='Текстовое описание')
    cta_text = models.CharField(max_length=255, verbose_name='Текст кнопки (СТА)', default='Вступить в движение')
    cta_link = models.URLField(verbose_name='Ссылка на Google Forms')


    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class AboutMovement(models.Model):
    description = models.CharField(max_length=155, verbose_name='Описание')
    advantage = models.TextField(verbose_name='Преимущество', blank=True, null=True)


    class Meta:
        verbose_name = 'О движении'
        verbose_name_plural = 'О движении'


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название мероприятия')
    description = models.TextField(verbose_name='Описание мероприятия')
    date = models.DateField(verbose_name='Дата проведения')


    class Meta:
        verbose_name = "Анонс мероприятия"
        verbose_name_plural = "Анонсы мероприятий"


class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement ,on_delete=models.CASCADE, related_name='images', verbose_name='Анонс')
    image = models.ImageField(upload_to='announcement_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Изображение анонса")


    class Meta:
        verbose_name = "Изображение анонса"
        verbose_name_plural = "Изображения анонсов"



class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name="Дата публикации")
    image = models.ImageField(
        upload_to='news_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Изображение новости"
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class BrandMaterial(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название материала")
    file = models.FileField(
        upload_to='brand_materials/',
        verbose_name="Файл",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'svg'])],
        help_text="Допустимые форматы: jpg, jpeg, png, pdf, svg"
    )

    class Meta:
        verbose_name = "Бренд-материал"
        verbose_name_plural = "Бренд-материалы"