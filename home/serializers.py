from rest_framework import serializers
from .models import (
    HomePage, Banner, BannerImage, AboutMovement, 
    Advantage, EventsModel, NewsModel, BrendMaterialModel
)

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ("id", "image")

class BannerSerializer(serializers.ModelSerializer):
    images = BannerImageSerializer(source="image", many=True, read_only=True)
    class Meta:
        model = Banner
        fields = ("id", "title", "description", "cta_text", "cta_link", "images")

class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ("id", "title", "text")

class AboutMovementSerializer(serializers.ModelSerializer):
    advantages = AdvantageSerializer(source="about_movement", many=True, read_only=True)
    class Meta:
        model = AboutMovement
        fields = ("id", "description", "advantages")

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsModel
        fields = ("id", "title", "data", "image", "short_text")

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ("id", "data", "news_image", "description")

class BrendMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrendMaterialModel
        fields = ("id", "title", "price", "image")

class HomePageSerializer(serializers.ModelSerializer):
    banners_list = BannerSerializer(source="Banner", many=True, read_only=True)
    about_blocks = AboutMovementSerializer(source="about_movement", many=True, read_only=True)
    events_list = EventsSerializer(source="events_items", many=True, read_only=True)
    news_list = NewsSerializer(source="news_items", many=True, read_only=True)
    merch_list = BrendMaterialSerializer(source="brend_items", many=True, read_only=True)

    class Meta:
        model = HomePage
        fields = (
            "id", "slug", "home_title",
            "banner", "banners_list",
            "about_movent", "about_blocks",
            "events", "events_list",
            "news", "news_list",
            "brend_material", "merch_list",
        )