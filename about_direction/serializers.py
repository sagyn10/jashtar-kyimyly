from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import History, Goals, Legislative, Management


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['title', 'description', 'image']


class GoalsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = ['title', 'description', 'image']


class LegislativeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Legislative
        fields = ['law', 'file', 'image']


class ManagementListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ['full_name', 'image', 'position']