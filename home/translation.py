from modeltranslation.translator import register, TranslationOptions
from .models import (
    Banner, AboutMovement, Advantage, HomePage, EventsModel,
    NewsModel, BrendMaterialModel
)

@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    fields = ("home_title", "banner", "about_movent", "events", "news", "brend_material")

@register(Banner)
class BannerTranslation(TranslationOptions):
    fields = ('title', 'description', 'cta_text')

@register(AboutMovement)
class AboutMovementTranslation(TranslationOptions):
    fields = ('description',)

@register(Advantage)
class AdvantageTranslation(TranslationOptions):
    fields = ("title", 'text',)

@register(EventsModel)
class EventsModelTranslation(TranslationOptions):
    fields = ("title", "short_text")

@register(NewsModel)
class NewsModelTranslation(TranslationOptions):
    fields = ("description",)

@register(BrendMaterialModel)
class BrendMaterialModelTranslation(TranslationOptions):
    fields = ("title",)