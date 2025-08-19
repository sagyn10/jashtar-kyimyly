from modeltranslation.translator import register, TranslationOptions
from .models import (Events, Projects, ActivityDirection, Departments, Results, News, BrandMaterial)



@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ActivityDirection)
class ActivityDirectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Departments)
class DepartmentsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Results)
class ResultsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class BrandMaterialTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)