from . import translation
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from _common.mixins import TranslatorMediaMixin
from .models import Banner, BannerImage, AboutMovement, BrandMaterial, Advantage, BrandMaterialImage

class BannerImageInline(admin.TabularInline):
    model = BannerImage
    extra = 0
    max_num = 10


@admin.register(Banner)
class BannerAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'description', 'cta_text', 'cta_link')
    list_display_links = ('description', )
    inlines = [BannerImageInline]


@admin.register(AboutMovement)
class AboutMovementAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('description',)

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'date')

class BrandMaterialImageInline(admin.TabularInline):
    model = BrandMaterialImage
    extra = 0
    max_num = 10

@admin.register(BrandMaterial)
class BrandMaterialAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'file')
    inlines = [BrandMaterialImageInline]

@admin.register(Advantage)
class AdvantageAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('pk',)
