from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import HomePage
from .serializers import HomePageSerializer

class HomePageDetailView(APIView):
    def get(self, request, *args, **kwargs):
        page = get_object_or_404(HomePage, slug="home")
        serializer = HomePageSerializer(page, context={'request': request})
        return Response(serializer.data)