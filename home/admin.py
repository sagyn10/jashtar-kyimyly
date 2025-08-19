from django.contrib import admin
from .models import HomeBanner, HomeAboutMovement, HomeAnnouncement, HomeNews, HomeBrandMaterial

@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'cta_text', 'cta_link')
    search_fields = ('description', 'cta_text')

@admin.register(HomeAboutMovement)
class HomeAboutMovementAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'advantage')
    search_fields = ('description', 'advantage')

@admin.register(HomeAnnouncement)
class HomeAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'announcement')
    search_fields = ('announcement__title', 'announcement__description')
    autocomplete_fields = ('announcement',)

@admin.register(HomeNews)
class HomeNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news')
    search_fields = ('news__title', 'news__description')
    autocomplete_fields = ('news',)

@admin.register(HomeBrandMaterial)
class HomeBrandMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_material')
    search_fields = ('brand_material__title',)
    autocomplete_fields = ('brand_material',)
