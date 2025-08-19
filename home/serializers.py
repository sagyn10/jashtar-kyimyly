from rest_framework import serializers
from .models import HomeBanner, HomeAboutMovement, HomeAnnouncement, HomeNews, HomeBrandMaterial
from content.serializers import AnnouncementSerializer, NewsSerializer, BrandMaterialSerializer

class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner
        fields = ['id', 'image', 'description', 'cta_text', 'cta_link']

class HomeAboutMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAboutMovement
        fields = ['id', 'description', 'advantage']

class HomeAnnouncementSerializer(serializers.ModelSerializer):
    announcement = AnnouncementSerializer()
    class Meta:
        model = HomeAnnouncement
        fields = ['id', 'announcement']

class HomeNewsSerializer(serializers.ModelSerializer):
    news = NewsSerializer()
    class Meta:
        model = HomeNews
        fields = ['id', 'news']

class HomeBrandMaterialSerializer(serializers.ModelSerializer):
    brand_material = BrandMaterialSerializer()
    class Meta:
        model = HomeBrandMaterial
        fields = ['id', 'brand_material']
