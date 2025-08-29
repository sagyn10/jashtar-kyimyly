from . import translation
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from _common.mixins import TranslatorMediaMixin
from .models import Banner, AboutMovement, BrandMaterial

@admin.register(Banner)
class BannerAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('description', 'cta_text', 'cta_link')

@admin.register(AboutMovement)
class AboutMovementAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('description',)

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'date')

@admin.register(BrandMaterial)
class BrandMaterialAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'file')