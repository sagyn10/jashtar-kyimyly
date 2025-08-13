from .serializers import EventsSerializer, ProjectsSerializer, GallerySerializer
from rest_framework import viewsets, generics, status
from .models import *
from drf_spectacular.utils import extend_schema
from .serializers import (EventsSerializer,
                          ProjectsSerializer,
                          ActivityDirectionSerializer,
                          DepartmentsListSerializers,
                          ResultsListSerializers,
                          NewsListSerializers)
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['content'])
class EventList(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


@extend_schema(tags=["content"])
class EventsDetail(generics.RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


@extend_schema(tags=['content'])
class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


@extend_schema(tags=["content"])
class ProjectsDetail(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

@extend_schema(tags=['content'])
class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


@extend_schema(tags=['content'])
class GalleryDetail(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

@extend_schema(tags=['content'])
class ActivityDirectionList(generics.ListAPIView):
    queryset = ActivityDirection.objects.all()
    serializer_class = ActivityDirectionSerializer

@extend_schema(tags=['content'])
class DepartmentsDetailAPIView(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsListSerializers

@extend_schema(tags=['content'])
class DepartmentsListAPIView(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsListSerializers

@extend_schema(tags=['content'])
class ResultsDetailAPIView(generics.RetrieveAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsListSerializers

@extend_schema(tags=['content'])
class ResultsListAPIView(generics.RetrieveAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsListSerializers


@extend_schema(tags=['content'])
class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers

@extend_schema(tags=['content'])
class NewsListAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers