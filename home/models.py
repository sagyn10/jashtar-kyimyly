from django.db import models
from content.models import News, Events, Announcement, BrandMaterial  # FK к content

class HomeBanner(models.Model):
    image = models.ImageField(upload_to='banners/')
    description = models.TextField()
    cta_text = models.CharField(max_length=255)
    cta_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Banner {self.id}"

class HomeAboutMovement(models.Model):
    description = models.TextField()
    advantage = models.TextField()

    def __str__(self):
        return "About Movement"

class HomeAnnouncement(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='home_announcements')

class HomeNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='home_news')

class HomeBrandMaterial(models.Model):
    brand_material = models.ForeignKey(BrandMaterial, on_delete=models.CASCADE, related_name='home_brand_materials')
