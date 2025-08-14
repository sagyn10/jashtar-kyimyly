from rest_framework import serializers
from .models import Banner, AboutMovement, Announcement, AnnouncementImage, News, BrandMaterial
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

ALLOWED_FORMATS = ['JPEG', 'JPG', 'PNG']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'description', 'cta_text', 'cta_link']


class AboutMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMovement
        fields = ['id', 'description', 'advantage']


class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ['id', 'image']

    def validate_image(self, image):
        img = Image.open(image)
        if img.format.upper() not in ALLOWED_FORMATS:
            raise serializers.ValidationError('Допустимые форматы: JPG, JPEG, PNG')
        return image


class AnnouncementSerializer(serializers.ModelSerializer):
    images = AnnouncementImageSerializer(many=True, required=False)

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description', 'date', 'images']

    def create(self, validated_data):
        images_data = self.initial_data.getlist('images')
        if len(images_data) > 10:
            raise serializers.ValidationError("Можно загрузить максимум 10 изображений.")

        announcement = Announcement.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            date=validated_data['date']
        )

        for image in images_data:
            AnnouncementImage.objects.create(announcement=announcement, image=image)

        return announcement


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'date', 'image']


class BrandMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandMaterial
        fields = ['id', 'title', 'file']