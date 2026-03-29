from rest_framework import serializers
from .models import Banner, BannerImage, AboutMovement, BrandMaterial, Advantage, BrandMaterialImage
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from content.models import News, Events

ALLOWED_FORMATS = ['JPEG', 'JPG', 'PNG']

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['id', 'image']


class BannerSerializer(serializers.ModelSerializer):
    images = BannerImageSerializer(many=True, read_only=True)
    class Meta:
        model = Banner
        fields = ['id', 'title', 'description', 'cta_text', 'cta_link', 'images']


class AboutMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMovement
        fields = ['id', 'description']

class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ['id', 'text']

class BrandMaterialImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandMaterialImage
        fields = ['id', 'image']
    

class BrandMaterialListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandMaterial
        fields = ['id', 'title', 'file', 'price']

class BrandMaterialDetailSerializer(serializers.ModelSerializer):
    images = BrandMaterialImageSerializer(many=True, read_only=True)
    class Meta:
        model = BrandMaterial
        fields = ['id', 'title', 'price', 'images', 'description']


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
    materials = BrandMaterialListSerializer(many=True)
    news = NewsSerializer(many=True)
    events = EventsSerializer(many=True)