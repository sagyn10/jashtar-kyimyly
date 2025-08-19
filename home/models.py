from django.db import models
from content.models import News, BrandMaterial, ActivityDirection

class HomeContentBlock(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='home_blocks',
        blank=True,
        null=True,
        verbose_name='Новости'
    )
    brand_material = models.ForeignKey(
        BrandMaterial,
        on_delete=models.CASCADE,
        related_name='home_blocks',
        blank=True,
        null=True,
        verbose_name='Бренд материалы'
    )
    announcement = models.ForeignKey(
        ActivityDirection,
        on_delete=models.CASCADE,
        related_name='home_blocks',
        blank=True,
        null=True,
        verbose_name='Анонс мероприятия'
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')

    class Meta:
        verbose_name = 'Блок контента на главной'
        verbose_name_plural = 'Блоки контента на главной'
        ordering = ['order']

    def __str__(self):
        blocks = []
        if self.news:
            blocks.append(f"Новости: {self.news.title}")
        if self.brand_material:
            blocks.append(f"БрендМатериал: {self.brand_material.title}")
        if self.announcement:
            blocks.append(f"Анонс: {self.announcement.title}")
        return " | ".join(blocks) or f"Блок #{self.id}"
