from modeltranslation.translator import register, TranslationOptions
from .models import HomeBanner, HomeAboutMovement

@register(HomeBanner)
class HomeBannerTranslationOptions(TranslationOptions):
    fields = ('description', 'cta_text')

@register(HomeAboutMovement)
class HomeAboutMovementTranslationOptions(TranslationOptions):
    fields = ('description', 'advantage')
