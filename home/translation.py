from modeltranslation.translator import register, TranslationOptions
from .models import Banner, AboutMovement, Announcement, News, BrandMaterial

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('description', 'cta_text')

@register(AboutMovement)
class AboutMovementTranslationOptions(TranslationOptions):
    fields = ('description', 'advantage')

@register(Announcement)
class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(BrandMaterial)
class BrandMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)
