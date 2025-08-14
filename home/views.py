from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Banner, AboutMovement, Announcement, News, BrandMaterial
from .serializers import (
    BannerSerializer,
    AboutMovementSerializer,
    AnnouncementSerializer,
    NewsSerializer,
    BrandMaterialSerializer
)

@extend_schema(tags=['content'])
class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

@extend_schema(tags=['content'])
class AboutMovementList(generics.ListAPIView):
    queryset = AboutMovement.objects.all()
    serializer_class = AboutMovementSerializer

@extend_schema(tags=['content'])
class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

@extend_schema(tags=['content'])
class AnnouncementDetail(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

@extend_schema(tags=['content'])
class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

@extend_schema(tags=['content'])
class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

@extend_schema(tags=['content'])
class BrandMaterialList(generics.ListAPIView):
    queryset = BrandMaterial.objects.all()
    serializer_class = BrandMaterialSerializer
