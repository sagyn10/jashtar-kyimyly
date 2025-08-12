from modeltranslation.translator import register, TranslationOptions
from .models import Events, Projects, ActivityDirection, Departments, Results, News, Gallery, VideoArchive


@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(VideoArchive)
class VideoArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)

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