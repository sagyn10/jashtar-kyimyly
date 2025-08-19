from rest_framework import serializers
from .models import HomeContentBlock
from content.serializers import NewsListSerializers, BrandMaterialSerializer
from content.serializers import ActivityDirectionSerializer

class HomeContentBlockSerializer(serializers.ModelSerializer):
    news = NewsListSerializers(read_only=True)
    brand_material = BrandMaterialSerializer(read_only=True)
    announcement = ActivityDirectionSerializer(read_only=True)

    class Meta:
        model = HomeContentBlock
        fields = ['id', 'news', 'brand_material', 'announcement', 'order']
