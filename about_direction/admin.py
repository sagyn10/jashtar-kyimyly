from . import translation
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from _common.mixins import TranslatorMediaMixin
from .models import History, Goals, Legislative, Management

@admin.register(History)
class HistoryAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'description', 'image')

@admin.register(Goals)
class  GoalsAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('title', 'description', 'image')


@admin.register(Legislative)
class LegislativeAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('law', 'file', 'image')


@admin.register(Management)
class ManagementAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('image', 'full_name', 'position')