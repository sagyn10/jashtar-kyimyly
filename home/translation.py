from modeltranslation.translator import register, TranslationOptions
from .models import Banner, AboutMovement, Advantage, BrandMaterial


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'cta_text')


@register(AboutMovement)
class AboutMovementTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(BrandMaterial)
class BrandMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)
