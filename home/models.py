from decimal import Decimal

from django.db import models
from django.core.validators import FileExtensionValidator
from content.models import News, Events


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название баннера', null=False, blank=True)
    description = models.CharField(max_length=255, verbose_name='Текстовое описание')
    cta_text = models.CharField(max_length=255, verbose_name='Текст кнопки (СТА)', default='Вступить в движение')
    cta_link = models.URLField(verbose_name='Ссылка на Google Forms')
    

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
    
    def __str__(self):
        return self.description


class BannerImage(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='image')
    image = models.FileField(
        upload_to='banners/',
        verbose_name="Изображение (SVG)",
        validators=[FileExtensionValidator(allowed_extensions=['svg'])],
        help_text="Загружайте только изображения в формате .svg"
    )

    class Meta:
        verbose_name = "Изображение баннера"
        verbose_name_plural = "Изображения баннеров"

    def __str__(self):
        return f"{self.banner.description} - изображение"


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
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена материала', default=Decimal('0.00'))
    description = models.TextField('Описание материала', null=True, blank=True)

    class Meta:
        verbose_name = "Бренд-материал"
        verbose_name_plural = "Бренд-материалы"

class BrandMaterialImage(models.Model):
    brand_material = models.ForeignKey(BrandMaterial, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(
        upload_to='brand_materials/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'svg'])],
        help_text="Допустимые форматы: jpg, jpeg, png, pdf, svg"
    )

    class Meta:
        verbose_name = "Изображение материала"
        verbose_name_plural = "Изображения материала"

    def __str__(self):
        return f"{self.brand_material.title} - изображение"
    