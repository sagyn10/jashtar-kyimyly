from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import (
    Events, Projects, Gallery, GalleryImage, VideoArchive, ActivityDirection,
    Departments, Results, News, Course
)
from .serializers import (
    EventSerializer, ProjectDetailSerializer, ProjectListSerializer, GallerySerializer, GalleryImageSerializer,
    VideoArchiveSerializer, ActivityDirectionSerializer,
    DepartmentSerializer, ResultsSerializer, NewsSerializer, CourseSerializer
)


@extend_schema(tags=['content'], description="Получение списка мероприятий")
class EventList(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о мероприятии")
class EventsDetail(RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer


@extend_schema(tags=['content'], description="Получение списка проектов")
class ProjectList(ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectListSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о проекте")
class ProjectsDetail(RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectDetailSerializer


@extend_schema(
    tags=['content'],
    description="Получение изображений галереи",
        parameters=[
        OpenApiParameter(
            name='limit',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Максимальное количество изображений'
        )
    ]
)
class GalleryImageList(ListAPIView):
    serializer_class = GalleryImageSerializer
    queryset = GalleryImage.objects.order_by('pk')


    def get_queryset(self):
        queryset = super().get_queryset()
        limit = self.request.query_params.get('limit')
        if limit is not None:
            try:
                limit = int(limit)
                queryset = queryset[:limit]
            except ValueError:
                pass
        return queryset


class GalleryPagination(PageNumberPagination):
    max_page_size = 30
    page_query_param = 'page'
    page_size_query_param = 'size'


@extend_schema(tags=['content'], description="Получение списка галерей")
class GalleryList(ListAPIView):
    queryset = Gallery.objects.all()
    pagination_class = GalleryPagination
    serializer_class = GallerySerializer


@extend_schema(tags=['content'], description="Получение детальной информации о галерее")
class GalleryDetail(RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


@extend_schema(tags=['content'], description="Получение списка видеоархивов")
class VideoArchiveList(ListAPIView):
    queryset = VideoArchive.objects.all()
    serializer_class = VideoArchiveSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о видеоархиве")
class VideoArchiveDetail(RetrieveAPIView):
    queryset = VideoArchive.objects.all()
    serializer_class = VideoArchiveSerializer


@extend_schema(tags=['content'], description="Получение списка направлений деятельности")
class ActivityDirectionList(ListAPIView):
    queryset = ActivityDirection.objects.order_by('id').all()
    serializer_class = ActivityDirectionSerializer


# @extend_schema(tags=['content'], description="Получение детальной информации о направлении деятельности")
# class ActivityDirectionDetail(RetrieveAPIView):
#     queryset = ActivityDirection.objects.all()
#     serializer_class = ActivityDirectionSerializer
#     lookup_field = 'id'


@extend_schema(tags=['content'], description="Получение списка региональных отделений")
class DepartmentsListAPIView(ListAPIView):
    queryset = Departments.objects.prefetch_related('employees').all()
    serializer_class = DepartmentSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о региональном отделении")
class DepartmentsDetailAPIView(RetrieveAPIView):
    queryset = Departments.objects.prefetch_related('employees').all()
    serializer_class = DepartmentSerializer


@extend_schema(tags=['content'], description="Получение списка результатов")
class ResultsListAPIView(ListAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о результате")
class ResultsDetailAPIView(RetrieveAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer


@extend_schema(tags=['content'], description="Получение списка новостей")
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema(tags=['content'], description="Получение детальной информации о новости")
class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema(tags=['content'], description="Получение списка курсов")
class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
