from django.contrib import admin
from .models import Banner, AboutMovement, Announcement, AnnouncementImage, BrandMaterial

class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 0
    max_num = 10

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('description', 'cta_text', 'cta_link')

@admin.register(AboutMovement)
class AboutMovementAdmin(admin.ModelAdmin):
    list_display = ('description', 'advantage')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    inlines = [AnnouncementImageInline]

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'date')

@admin.register(BrandMaterial)
class BrandMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
