from rest_framework import viewsets
from .models import HomeContentBlock
from .serializers import HomeContentBlockSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Home Announcements'])
class HomeContentBlockViewSet(viewsets.ModelViewSet):
    queryset = HomeContentBlock.objects.all().order_by('order')
    serializer_class = HomeContentBlockSerializer
