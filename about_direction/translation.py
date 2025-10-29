from modeltranslation.translator import register, TranslationOptions
from .models import History, Goals, Legislative, Management

@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Goals)
class GoalsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Legislative)
class LegislativeTranslationOptions(TranslationOptions):
    fields = ('law', 'description')

@register(Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position')
