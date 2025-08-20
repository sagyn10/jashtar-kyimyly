from django.contrib import admin
from .models import HomeContentBlock

@admin.register(HomeContentBlock)
class HomeContentBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'brand_material', 'announcement', 'order')