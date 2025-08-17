from rest_framework import serializers
from .models import Events, EventImage, Projects, ProjectsImage, Gallery, GalleryImage, VideoArchive, ActivityDirection, Departments, DepartmentImage, Results, News

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'event', 'image']

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    class Meta:
        model = Events
        fields = ['id', 'title', 'description', 'slug', 'date', 'event_status', 'images']

class ProjectsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsImage
        fields = ['id', 'project', 'image']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectsImageSerializer(many=True, read_only=True)
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'slug', 'images']

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'gallery', 'image']

class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'date', 'images']

class VideoArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoArchive
        fields = ['id', 'title', 'video_url']

class ActivityDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDirection
        fields = ['id', 'title', 'description']

class DepartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentImage
        fields = ['id', 'department', 'image']

class DepartmentSerializer(serializers.ModelSerializer):
    images = DepartmentImageSerializer(many=True, read_only=True)
    class Meta:
        model = Departments
        fields = ['id', 'title', 'description', 'address', 'image', 'images']

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ['id', 'title', 'description']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'date', 'image', 'slug']