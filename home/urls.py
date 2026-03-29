from django.urls import path, include
from rest_framework import routers
from .views import (
    BannerList,
    AboutMovementList,
    # AnnouncementList,
    # AnnouncementDetail,
    # NewsList,
    # NewsDetail,
    AdvantageList,
    BrandMaterialList,
    BrandMaterialDetail,
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('banners/', BannerList.as_view(), name='banner-list'),
    path('about-movement/', AboutMovementList.as_view(), name='about-movement-list'),
    # path('announcements/', AnnouncementList.as_view(), name='announcement-list'),
    # path('announcements/<int:pk>/', AnnouncementDetail.as_view(), name='announcement-detail'),
    # path('news/', NewsList.as_view(), name='news-list'),
    # path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),

    path('advantages/', AdvantageList.as_view(), name='advantages-list'),
    path('brand-materials/', BrandMaterialList.as_view(), name='brand-material-list'),
    path('brand-materials/<int:id>/', BrandMaterialDetail.as_view(), name='brand-material-detail'),
    # path('home/', HomePageView.as_view(), name='home')
]