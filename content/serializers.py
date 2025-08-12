from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from .models import (
    Events, EventImage, Projects, ProjectsImage, Gallery, GalleryImage,
    VideoArchive, ActivityDirection, Departments, DepartmentImage, Results, News
)

ALLOWED_FORMATS = ['JPEG', 'JPG', 'PNG']


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('id', 'image')

    def validate_image(self, image):
        img = Image.open(image)
        if img.format.upper() not in ALLOWED_FORMATS:
            raise serializers.ValidationError('Допустимые форматы: JPG, JPEG, PNG')
        return image


class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Events
        fields = ('id', 'title', 'description', 'date', 'event_status', 'slug', 'images', 'uploaded_images')

    def validate_uploaded_images(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("Можно загрузить максимум 10 изображений.")
        return value

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images', [])
        event = Events.objects.create(**validated_data)
        for image in images_data:
            EventImage.objects.create(event=event, image=image)
        return event

    def update(self, instance, validated_data):
        images_data = validated_data.pop('uploaded_images', None)
        instance = super().update(instance, validated_data)
        if images_data:
            if instance.images.count() + len(images_data) > 10:
                raise serializers.ValidationError("Нельзя превысить лимит в 10 изображений.")
            for image in images_data:
                EventImage.objects.create(event=instance, image=image)
        return instance


class ProjectsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsImage
        fields = ('id', 'image')

    def validate_image(self, image):
        img = Image.open(image)
        if img.format.upper() not in ALLOWED_FORMATS:
            raise serializers.ValidationError('Допустимые форматы: JPG, JPEG, PNG')
        return image


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectsImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Projects
        fields = ('id', 'title', 'description', 'slug', 'images', 'uploaded_images')

    def validate_uploaded_images(self, value):
        if len(value) > 5:
            raise serializers.ValidationError("Можно загрузить максимум 5 изображений.")
        return value

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images', [])
        project = Projects.objects.create(**validated_data)
        for image in images_data:
            ProjectsImage.objects.create(project=project, image=image)
        return project

    def update(self, instance, validated_data):
        images_data = validated_data.pop('uploaded_images', None)
        instance = super().update(instance, validated_data)
        if images_data:
            if instance.images.count() + len(images_data) > 5:
                raise serializers.ValidationError("Нельзя превысить лимит в 5 изображений.")
            for image in images_data:
                ProjectsImage.objects.create(project=instance, image=image)
        return instance


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ('id', 'image')

    def validate_image(self, image):
        img = Image.open(image)
        if img.format.upper() not in ALLOWED_FORMATS:
            raise serializers.ValidationError('Допустимые форматы: JPG, JPEG, PNG')
        return image

    def create(self, validated_data):
        image = validated_data.get('image')
        img = Image.open(image)
        img = img.convert('RGB')
        output_io = BytesIO()
        img.save(output_io, format='JPEG', quality=70)
        compressed_image = ContentFile(output_io.getvalue(), image.name)
        validated_data['image'] = compressed_image
        return super().create(validated_data)


class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'date', 'images', 'uploaded_images')

    def validate_uploaded_images(self, value):
        if len(value) > 15:
            raise serializers.ValidationError("Можно загрузить максимум 15 изображений.")
        return value

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images', [])
        gallery = Gallery.objects.create(**validated_data)
        for image in images_data:
            serializer = GalleryImageSerializer(data={'image': image})
            serializer.is_valid(raise_exception=True)
            serializer.save(gallery=gallery)
        return gallery

    def update(self, instance, validated_data):
        images_data = validated_data.pop('uploaded_images', None)
        instance = super().update(instance, validated_data)
        if images_data:
            if instance.images.count() + len(images_data) > 15:
                raise serializers.ValidationError("Нельзя превысить лимит в 15 изображений.")
            for image in images_data:
                serializer = GalleryImageSerializer(data={'image': image})
                serializer.is_valid(raise_exception=True)
                serializer.save(gallery=instance)
        return instance


class VideoArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoArchive
        fields = ('id', 'title', 'video_url')

    def validate_video_url(self, value):
        if not ('youtube.com' in value or 'youtu.be' in value):
            raise serializers.ValidationError("Ссылка должна быть на YouTube.")
        return value


class ActivityDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDirection
        fields = ('id', 'title', 'description', 'slug')


class DepartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentImage
        fields = ('id', 'image')

    def validate_image(self, image):
        img = Image.open(image)
        if img.format.upper() not in ALLOWED_FORMATS:
            raise serializers.ValidationError('Допустимые форматы: JPG, JPEG, PNG')
        return image


class DepartmentSerializer(serializers.ModelSerializer):
    images = DepartmentImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Departments
        fields = ('id', 'title', 'description', 'address', 'images', 'uploaded_images')

    def validate_uploaded_images(self, value):
        if len(value) > 5:
            raise serializers.ValidationError("Можно загрузить максимум 5 изображений.")
        return value

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images', [])
        department = Departments.objects.create(**validated_data)
        for image in images_data:
            DepartmentImage.objects.create(department=department, image=image)
        return department

    def update(self, instance, validated_data):
        images_data = validated_data.pop('uploaded_images', None)
        instance = super().update(instance, validated_data)
        if images_data:
            if instance.images.count() + len(images_data) > 5:
                raise serializers.ValidationError("Нельзя превысить лимит в 5 изображений.")
            for image in images_data:
                DepartmentImage.objects.create(department=instance, image=image)
        return instance


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ('id', 'title', 'description')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'date', 'image', 'slug')