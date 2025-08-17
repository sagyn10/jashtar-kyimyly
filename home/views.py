from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Banner, AboutMovement, Announcement, News, BrandMaterial
from .serializers import (
    BannerSerializer,
    AboutMovementSerializer,
    AnnouncementSerializer,
    # NewsSerializer,
    BrandMaterialSerializer
)

@extend_schema(tags=['home'], description="Получение списка баннеров")
class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

@extend_schema(tags=['home'], description="Получение детальной информации о баннере")
class BannerDetail(generics.RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    lookup_field = 'id'


@extend_schema(tags=['home'], description="Получение информации о движении")
class AboutMovementList(generics.ListAPIView):
    queryset = AboutMovement.objects.all()
    serializer_class = AboutMovementSerializer

@extend_schema(tags=['home'], description="Получение детальной информации о движении")
class AboutMovementDetail(generics.RetrieveAPIView):
    queryset = AboutMovement.objects.all()
    serializer_class = AboutMovementSerializer
    lookup_field = 'id'


@extend_schema(tags=['home'], description="Получение списка анонсов мероприятий")
class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

@extend_schema(tags=['home'], description="Получение детальной информации о анонсе мероприятия")
class AnnouncementDetail(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'id'


# @extend_schema(tags=['home'], description="Получение списка новостей")
# class NewsList(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#
# @extend_schema(tags=['home'], description="Получение детальной информации о новости")
# class NewsDetail(generics.RetrieveAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     lookup_field = 'id'


@extend_schema(tags=['home'], description="Получение списка бренд-материалов")
class BrandMaterialList(generics.ListAPIView):
    queryset = BrandMaterial.objects.all()
    serializer_class = BrandMaterialSerializer

@extend_schema(tags=['home'], description="Получение детальной информации о бренд-материале")
class BrandMaterialDetail(generics.RetrieveAPIView):
    queryset = BrandMaterial.objects.all()
    serializer_class = BrandMaterialSerializer
    lookup_field = 'id'
