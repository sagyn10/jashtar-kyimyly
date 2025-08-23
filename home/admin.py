from django.contrib import admin
from .models import Banner, AboutMovement, BrandMaterial

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('description', 'cta_text', 'cta_link')

@admin.register(AboutMovement)
class AboutMovementAdmin(admin.ModelAdmin):
    list_display = ('description',)

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'date')

@admin.register(BrandMaterial)
class BrandMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
