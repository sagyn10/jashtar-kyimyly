from rest_framework import serializers

from .models import (
    Events, EventImage, Projects,
    ProjectsImage, Gallery, GalleryImage,
    VideoArchive, ActivityDirection, Departments, 
    Results, News, Employee, EducationMaterial, Course)

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'event', 'image']

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    class Meta:
        model = Events
        fields = ['id', 'title', 'description', 'date', 'event_status', 'images', 'time', 'place']

class ProjectsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsImage
        fields = ['id', 'project', 'image']

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'image']

class ProjectDetailSerializer(serializers.ModelSerializer):
    images = ProjectsImageSerializer(many=True, read_only=True)
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'image', 'goals', 'tasks', 'images']

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'gallery', 'image', 'title', 'date']

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
        fields = ['id', 'title', 'short_description', 'telegram_link', 'instagram_link', 'description', 'image']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'image']

class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = Departments
        fields = ['id', 'title', 'description', 'address', 'employees']

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ['id', 'title', 'description']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'date', 'image']

class EducationMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationMaterial
        fields = ['id', 'title', 'attachment_type', 'attachment', 'link']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'image', 'link']
