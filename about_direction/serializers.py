from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import History, HistoryImage, Goals, GoalImage, Legislative, Management

class HistoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryImage
        fields = ['id', 'image']


class HistorySerializers(serializers.ModelSerializer):
    images = HistoryImageSerializer(many=True, read_only=True)
    class Meta:
        model = History
        fields = ['id', 'title', 'description', 'image', 'images']


class GoalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalImage
        fields = ['id', 'image']


class GoalsListSerializers(serializers.ModelSerializer):
    images = GoalImageSerializer(many=True, read_only=True)
    class Meta:
        model = Goals
        fields = ['id', 'title', 'description', 'image', 'images']


class LegislativeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Legislative
        fields = ['id', 'law', 'description', 'file', 'date']


class ManagementListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ['id', 'full_name', 'image', 'position']
