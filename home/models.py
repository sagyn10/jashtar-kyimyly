from django.db import models
from django.core.validators import FileExtensionValidator
from content.models import News, Events


class Banner(models.Model):
    description = models.CharField(max_length=255, verbose_name='Текстовое описание')
    cta_text = models.CharField(max_length=255, verbose_name='Текст кнопки (СТА)', default='Вступить в движение')
    cta_link = models.URLField(verbose_name='Ссылка на Google Forms')


    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class BannerImage(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='Баннеры')
    image = models.FileField(
        upload_to='banners/',
        verbose_name="Изображение (SVG)",
        validators=[FileExtensionValidator(allowed_extensions=['svg'])],
        help_text="Загружайте только изображения в формате .svg"
    )

    class Meta:
        verbose_name = "Изображение баннера"
        verbose_name_plural = "Изображения баннеров"


class AboutMovement(models.Model):
    description = models.CharField(max_length=155, verbose_name='Описание')

    class Meta:
        verbose_name = 'О движении'
        verbose_name_plural = 'О движении'


class Advantage(models.Model):
    text = models.TextField(max_length=400, verbose_name='Преимущество')

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


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