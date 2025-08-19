from rest_framework import serializers
from .models import Events, Projects, EventImage, ProjectsImage, GalleryImage, Gallery
from drf_spectacular.utils import extend_schema_field
from .models import Gallery, GalleryImage
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import (Events, Projects, EventImage,
                     ProjectsImage, ActivityDirection,
                     Departments, Results, News, BrandMaterial)


class ActivityDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDirection
        fields = 'title', 'description'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsImage
        fields = ('id', 'image')


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('id', 'image')


class ProjectsSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, required=False)

    class Meta:
        model = Projects
        fields = ('id', 'title', 'description', 'images')

    def create(self, validated_data):
        images_data = self.initial_data.getlist('images')
        if len(images_data) > 5:
            raise serializers.ValidationError("Можно загрузить максимум 5 изображений.")

        project = Projects.objects.create(
            title=validated_data['title'],
            description=validated_data['description']
        )

        for image in images_data:
            ProjectsImage.objects.create(project=project, image=image)
        return project


class EventsSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, required=False)

    class Meta:
        model = Events
        fields = ('id', 'title', 'description', 'date', 'images')

    def create(self, validated_data):
        images_data = self.initial_data.getlist('images')
        if len(images_data) > 10:
            raise serializers.ValidationError("Можно загрузить максимум 10 изображений.")

        event = Events.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            date=validated_data['date']
        )

        for image in images_data:
            EventImage.objects.create(event=event, image=image)
        return event


ALLOWED_FORMATS = ['JPEG', 'JPG', 'PNG']

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ('id', 'image')

    def validate_image(self, image):
        img = Image.open(image)
        if img.format.upper() not in ALLOWED_FORMATS:
            raise serializers.ValidationError('Допустимые форматы: JPG, JPEG, PNG')
        return image

    def compress_image(self, image):
        img = Image.open(image)
        output_io = BytesIO()
        img.save(output_io, format='JPEG', quality=70)
        return ContentFile(output_io.getvalue(), image.name)

    def create(self, validated_data):
        image = validated_data.get('image')
        compressed = self.compress_image(image)
        validated_data['image'] = compressed
        return super().create(validated_data)


class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, required=False)

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'images')

    def create(self, validated_data):
        images_data = self.initial_data.getlist('images')
        if len(images_data) > 15:
            raise serializers.ValidationError("Можно загрузить максимум 15 изображений.")

        gallery = Gallery.objects.create(
            title=validated_data['title']
        )

        for image in images_data:
            serializer = GalleryImageSerializer(data={'image': image})
            serializer.is_valid(raise_exception=True)
            serializer.save(gallery=gallery)
        return gallery

class DepartmentsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['title', 'description', 'address', 'image']


class ResultsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ['title', 'description']


class NewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description', 'date']



class BrandMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandMaterial
        fields = ['id', 'title', 'description', 'slug', 'image']
