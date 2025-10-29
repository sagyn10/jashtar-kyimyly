from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema
from .models import Banner, AboutMovement, BrandMaterial, Advantage
from .serializers import (
    BannerSerializer,
    AboutMovementSerializer,
    BrandMaterialListSerializer,
    BrandMaterialDetailSerializer,
    AdvantageSerializer
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


@extend_schema(tags=['home'], description='Получение информации о преимуществах')
class AdvantageList(generics.ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer


@extend_schema(tags=['home'], description='Получение детальной информации о преимуществах')
class AdvantageDetail(generics.ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer
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


# @extend_schema(tags=['home'], description="Получение списка бренд-материалов")
# class BrandMaterialList(generics.ListAPIView):
#     queryset = BrandMaterial.objects.all()
#     serializer_class = BrandMaterialSerializer

@extend_schema(tags=['home'], description="Получение детальной информации о бренд-материале")
class BrandMaterialDetail(generics.RetrieveAPIView):
    queryset = BrandMaterial.objects.all()
    serializer_class = BrandMaterialDetailSerializer
    lookup_field = 'id'

# from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView
# from rest_framework.response import Response
# 
# from .models import Banner, AboutMovement, Advantage, BrandMaterial
# from content.models import News, Events
# from .serializers import (
#     HomePageSerializer, BannerSerializer,
#     AboutMovementSerializer, AdvantageSerializer,
#     BrandMaterialSerializer, NewsSerializer, EventsSerializer
# )
# from drf_spectacular.utils import extend_schema




# @extend_schema(tags=['home'],  description="home")
# class HomePageView(APIView):
#     def get(self, request):
#         data = {
#             "banners": Banner.objects.prefetch_related('image').all(),
#             "about": AboutMovement.objects.all(),
#             "advantages": Advantage.objects.all(),
#             "materials": BrandMaterial.objects.all(),
#             "news": News.objects.all().order_by('-date')[:5],
#             "events": Events.objects.all().order_by('-date')[:5],
#         }

#         serializer = HomePageSerializer(data)
#         return Response(serializer.data)
    

class BrandMaterialsPagination(PageNumberPagination):
    max_page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'


@extend_schema(tags=['home'], description="Получение списка бренд-материалов")
class BrandMaterialList(generics.ListAPIView):
    """
    Class-based view for retirving paginated list of BrandMaterials objects.

    Attributes:
        serializer_class: Serializer of model objects.
        pagination_class: Results pagination class
        queryset: Model object retrieving queryset.
    """
    serializer_class = BrandMaterialListSerializer
    pagination_class = BrandMaterialsPagination
    queryset = BrandMaterial.objects.order_by('pk').all()
    