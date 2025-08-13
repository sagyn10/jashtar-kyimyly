from .serializers import HistorySerializers, GoalsListSerializers, LegislativeListSerializers, ManagementListSerializers
from rest_framework import generics, status
from .models import History, Goals, Management, Legislative
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['about_direction'])
class HistoryListAPIView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers

@extend_schema(tags=['about_direction'])
class HistoryDetailAPIView(generics.RetrieveAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers

@extend_schema(tags=['about_direction'])
class GoalsListAPIView(generics.ListAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsListSerializers

@extend_schema(tags=['about_direction'])
class GoalsDetailAPIView(generics.RetrieveAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsListSerializers

@extend_schema(tags=['about_direction'])
class LegislativeListAPIView(generics.ListAPIView):
    queryset = Legislative.objects.all()
    serializer_class = LegislativeListSerializers

@extend_schema(tags=['about_direction'])
class LegislativeDetailAPIView(generics.RetrieveAPIView):
    queryset = Legislative.objects.all()
    serializer_class = LegislativeListSerializers

@extend_schema(tags=['about_direction'])
class ManagementListAPIView(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementListSerializers

@extend_schema(tags=['about_direction'])
class ManagementDetailAPIView(generics.RetrieveAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementListSerializers