from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import HomeBanner, HomeAboutMovement, HomeAnnouncement, HomeNews, HomeBrandMaterial
from .serializers import (
    HomeBannerSerializer,
    HomeAboutMovementSerializer,
    HomeAnnouncementSerializer,
    HomeNewsSerializer,
    HomeBrandMaterialSerializer
)

@extend_schema(tags=['home'])
class BannerList(generics.ListAPIView):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer

@extend_schema(tags=['home'])
class AboutMovementList(generics.ListAPIView):
    queryset = HomeAboutMovement.objects.all()
    serializer_class = HomeAboutMovementSerializer

@extend_schema(tags=['home'])
class AnnouncementList(generics.ListAPIView):
    queryset = HomeAnnouncement.objects.all()
    serializer_class = HomeAnnouncementSerializer

@extend_schema(tags=['home'])
class NewsList(generics.ListAPIView):
    queryset = HomeNews.objects.all()
    serializer_class = HomeNewsSerializer

@extend_schema(tags=['home'])
class BrandMaterialList(generics.ListAPIView):
    queryset = HomeBrandMaterial.objects.all()
    serializer_class = HomeBrandMaterialSerializer
