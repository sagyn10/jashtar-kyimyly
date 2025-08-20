from django.contrib import admin
from .models import Events, Projects, EventImage, ProjectsImage, GalleryImage, Gallery
from .models import Events, Projects, EventImage, ProjectsImage, ActivityDirection, Departments, Results, BrandMaterial
from modeltranslation.translator import register, TranslationOptions

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


@admin.register(Events)
class EventsAdmin(TranslationOptions):
    list_display = ('title', 'description', 'date')
    inlines = [EventImageInline]
    exclude = ('slug',)


@admin.register(Projects)
class ProjectsAdmin(TranslationOptions):
    list_display = ('title', 'description')
    inlines = [ProjectImageInline]
    exclude = ('slug',)


@admin.register(Gallery)
class GalleryAdmin(TranslationOptions):
    list_display = ('title', 'date')
    inlines = [GalleryImageInline]
    exclude = ('slug',)
    fields = ('title',)

@admin.register(ActivityDirection)
class ActivityDirectionAdin(TranslationOptions):
    list_display = ('title', 'description')

@admin.register(Departments)
class DepartmentsAdmin(TranslationOptions):
    list_display = ('title', 'description', 'address', 'image')


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(BrandMaterial)
class BrandMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('title',)
