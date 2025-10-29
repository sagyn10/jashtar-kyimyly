from modeltranslation.translator import register, TranslationOptions
from .models import Events, Employee, Projects, ActivityDirection, Departments, Results, News, Gallery, GalleryImage, VideoArchive, EducationMaterial, Course


@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'goals', 'tasks')


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(VideoArchive)
class VideoArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ActivityDirection)
class ActivityDirectionTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


@register(Departments)
class DepartmentsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Results)
class ResultsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('name', 'position')

@register(GalleryImage)
class GalleryImageTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(EducationMaterial)
class EducationMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
