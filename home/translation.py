from modeltranslation.translator import translator, TranslationOptions
from .models import HomeContentBlock

class HomeContentBlockTranslationOptions(TranslationOptions):
    fields = ('news', 'brand_material', 'announcement',)

translator.register(HomeContentBlock, HomeContentBlockTranslationOptions)
