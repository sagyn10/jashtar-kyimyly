from django.urls import path
from .views import HomePageDetailView

urlpatterns = [
    path('home/', HomePageDetailView.as_view(), name='home-page'),
]