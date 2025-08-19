from django.urls import path
from .views import BannerList, AboutMovementList, AnnouncementList, NewsList, BrandMaterialList

urlpatterns = [
    path('banners/', BannerList.as_view(), name='home-banners'),
    path('about-movement/', AboutMovementList.as_view(), name='home-about-movement'),
    path('announcements/', AnnouncementList.as_view(), name='home-announcements'),
    path('news/', NewsList.as_view(), name='home-news'),
    path('brand-materials/', BrandMaterialList.as_view(), name='home-brand-materials'),
]
