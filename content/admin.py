from django.contrib import admin
from .models import (
    Events, EventImage,
    Projects, ProjectsImage,
    Gallery, GalleryImage,
    VideoArchive,
    ActivityDirection,
    Departments, DepartmentImage,
    Results, News
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


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
    max_num = 15


class DepartmentImageInline(admin.TabularInline):
    model = DepartmentImage
    extra = 0
    max_num = 5


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


@admin.register(Gallery)
class GalleryAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'date')
    inlines = [GalleryImageInline]
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
    inlines = [DepartmentImageInline]
    search_fields = ('title', 'address')


@admin.register(Results)
class ResultsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(News)
class NewsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)