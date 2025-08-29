from . import translation
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from _common.mixins import TranslatorMediaMixin
from .models import History, Goals, Legislative, Management

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

@admin.register(Goals)
class  GoalsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')


@admin.register(Legislative)
class LegislativeAdmin(admin.ModelAdmin):
    list_display = ('law', 'file', 'image')


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ('image', 'full_name', 'position')
class ManagementAdmin(TranslatorMediaMixin, TranslationAdmin):
    list_display = ('image', 'full_name', 'position')


