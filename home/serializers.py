from rest_framework import serializers
from .models import Banner, AboutMovement, BrandMaterial, Advantage
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from content.models import News, Events

ALLOWED_FORMATS = ['JPEG', 'JPG', 'PNG']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'description', 'cta_text', 'cta_link']


class AboutMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMovement
        fields = ['id', 'description']

class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ['id', 'text']


class BrandMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandMaterial
        fields = ['id', 'title', 'file']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'date', 'image']


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'title', 'description', 'date']


class HomePageSerializer(serializers.Serializer):
    banners = BannerSerializer(many=True)
    about = AboutMovementSerializer(many=True)
    advantages = AdvantageSerializer(many=True)
    materials = BrandMaterialSerializer(many=True)
    news = NewsSerializer(many=True)
    events = EventsSerializer(many=True)