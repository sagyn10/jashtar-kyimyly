from django.urls import path, include
from rest_framework import routers
from .views import (
    # BannerList,
    # AboutMovementList,
    # AnnouncementList,
    # AnnouncementDetail,
    # # NewsList,
    # # NewsDetail,
    # BrandMaterialList
    HomePageView
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # path('banners/', BannerList.as_view(), name='banner-list'),
    # path('about-movement/', AboutMovementList.as_view(), name='about-movement-list'),
    # path('announcements/', AnnouncementList.as_view(), name='announcement-list'),
    # path('announcements/<int:pk>/', AnnouncementDetail.as_view(), name='announcement-detail'),
    # # path('news/', NewsList.as_view(), name='news-list'),
    # # path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    # path('brand-materials/', BrandMaterialList.as_view(), name='brand-material-list'),
    path('home/', HomePageView.as_view(), name='home')
]
