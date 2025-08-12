from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import (
    Events, Projects, Gallery, VideoArchive, ActivityDirection,
    Departments, Results, News
)
from .serializers import (
    EventSerializer, ProjectSerializer, GallerySerializer,
    VideoArchiveSerializer, ActivityDirectionSerializer,
    DepartmentSerializer, ResultsSerializer, NewsSerializer
)


@extend_schema(tags=['content'], description="Получение списка мероприятий")
class EventList(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о мероприятии")
class EventsDetail(generics.RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'slug'


@extend_schema(tags=['content'], description="Получение списка проектов")
class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о проекте")
class ProjectsDetail(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


@extend_schema(tags=['content'], description="Получение списка галерей")
class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


@extend_schema(tags=['content'], description="Получение детальной информации о галерее")
class GalleryDetail(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = 'id'


@extend_schema(tags=['content'], description="Получение списка видеоархивов")
class VideoArchiveList(generics.ListAPIView):
    queryset = VideoArchive.objects.all()
    serializer_class = VideoArchiveSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о видеоархиве")
class VideoArchiveDetail(generics.RetrieveAPIView):
    queryset = VideoArchive.objects.all()
    serializer_class = VideoArchiveSerializer


@extend_schema(tags=['content'], description="Получение списка направлений деятельности")
class ActivityDirectionList(generics.ListAPIView):
    queryset = ActivityDirection.objects.all()
    serializer_class = ActivityDirectionSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о направлении деятельности")
class ActivityDirectionDetail(generics.RetrieveAPIView):
    queryset = ActivityDirection.objects.all()
    serializer_class = ActivityDirectionSerializer


@extend_schema(tags=['content'], description="Получение списка региональных отделений")
class DepartmentsListAPIView(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о региональном отделении")
class DepartmentsDetailAPIView(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


@extend_schema(tags=['content'], description="Получение списка результатов")
class ResultsListAPIView(generics.ListAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о результате")
class ResultsDetailAPIView(generics.RetrieveAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    lookup_field = 'id'


@extend_schema(tags=['content'], description="Получение списка новостей")
class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о новости")
class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
