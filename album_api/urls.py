from django.urls import path, include
from rest_framework.routers import DefaultRouter

from album_api import views

album_api_router = DefaultRouter()
album_api_router.register(r'albums', views.AlbumViewSet, basename='album')
album_api_router.register(r'photos', views.PhotoViewSet, basename='photo')

urlpatterns = [
    path('', include(album_api_router.urls)),
    path('hello', views.hello_world_view, name='hello_world'),
]
