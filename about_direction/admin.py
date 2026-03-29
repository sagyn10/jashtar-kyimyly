from . import translation
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from _common.mixins import TranslatorMediaMixin
from .models import History, HistoryImage, Goals, Legislative, Management, GoalImage


class GoalImageInline(admin.TabularInline):
    model = GoalImage
    extra = 0
    max_num = 5

class HistoryImageInline(admin.TabularInline):
    model = HistoryImage
    extra = 0
    max_num = 5


@admin.register(History)
class HistoryAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'description', 'image')
    inlines = [HistoryImageInline]


@admin.register(Goals)
class GoalsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'description', 'image')
    inlines = [GoalImageInline]


@admin.register(Legislative)
class LegislativeAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('law', 'file')


@admin.register(Management)
class ManagementAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('image', 'full_name', 'position')
    list_display_links = ('full_name', 'position') 
