from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .models import (
    HomePage, Banner, BannerImage, AboutMovement, 
    Advantage, EventsModel, NewsModel, BrendMaterialModel
)

# === INLINES ===


class BannerImageInline(admin.TabularInline):
    model = BannerImage
    extra = 1

class AdvantageInline(TranslationStackedInline):
    model = Advantage
    extra = 1



@admin.register(HomePage)
class HomePageAdmin(TranslationAdmin):
    list_display = ("home_title", "slug")
    search_fields = ("home_title",)
    
    def has_add_permission(self, request):
        
        if self.model.objects.exists():
            return False
       
        return super().has_add_permission(request)

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ("title", "page")
    autocomplete_fields = ("page",)
    inlines = [BannerImageInline]

@admin.register(AboutMovement)
class AboutMovementAdmin(TranslationAdmin):
    list_display = ("description", "page")
    autocomplete_fields = ("page",)
    inlines = [AdvantageInline]

@admin.register(EventsModel)
class EventsAdmin(TranslationAdmin):
    list_display = ("title", "data", "page")
    autocomplete_fields = ("page",)
    list_filter = ("page", "data")

@admin.register(NewsModel)
class NewsAdmin(TranslationAdmin):
    list_display = ("id", "data", "page")
    autocomplete_fields = ("page",)
    list_filter = ("page", "data")

@admin.register(BrendMaterialModel)
class BrendMaterialAdmin(TranslationAdmin):
    list_display = ("title", "price", "page")
    autocomplete_fields = ("page",)
    list_filter = ("page",)