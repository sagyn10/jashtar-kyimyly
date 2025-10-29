from . import translation
from django.contrib import admin
from .models import (
    Events, EventImage,
    Projects, ProjectsImage,
    Gallery, GalleryImage,
    VideoArchive,
    ActivityDirection,
    Departments,
    Results, News, Employee, EducationMaterial, Course
)
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from _common.mixins import TranslatorMediaMixin

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0
    max_num = 10


class ProjectImageInline(admin.TabularInline):
    model = ProjectsImage
    extra = 0
    max_num = 5


# class DepartmentImageInline(admin.TabularInline):
#     model = DepartmentImage
#     extra = 0
#     max_num = 5



@admin.register(Events)
class EventsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'date', 'event_status')
    inlines = [EventImageInline]
    exclude = ('slug',)
    search_fields = ('title',)
    list_filter = ('event_status', 'date')


@admin.register(Projects)
class ProjectsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title',)
    inlines = [ProjectImageInline]
    exclude = ('slug',)
    search_fields = ('title',)

@admin.register(GalleryImage)
class GalleryImagesAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'date', 'image')
    list_display_links = ('title', 'date')

@admin.register(Gallery)
class GalleryAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'date')
    exclude = ('slug',)
    search_fields = ('title',)
    list_filter = ('date',)


@admin.register(VideoArchive)
class VideoArchiveAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'video_url') 
    search_fields = ('title',)


@admin.register(ActivityDirection)
class ActivityDirectionAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(Departments)
class DepartmentsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'address')
    # inlines = [DepartmentImageInline]
    search_fields = ('title', 'address')


@admin.register(Employee)
class EmployeeAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')


@admin.register(Results)
class ResultsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(News)
class NewsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(EducationMaterial)
class EducationMaterialAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'attachment_type', 'attachment', 'link')
    search_fields = ('title', 'attachment_type')


@admin.register(Course)
class CourseAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'description', 'link')
    search_fields = ('title', 'description')
