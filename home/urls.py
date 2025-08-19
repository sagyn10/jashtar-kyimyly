from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeContentBlockViewSet

router = DefaultRouter()
router.register(r'home-announcements', HomeContentBlockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
