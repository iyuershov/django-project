from django.http import HttpRequest, JsonResponse
from rest_framework.viewsets import ModelViewSet

from album_api.models import Album, Photo
from album_api.serializers import AlbumSerializer, PhotoSerializer


def hello_world_view(request: HttpRequest) -> JsonResponse:
    """
    Метод для тестирования инициализации приложения
    :param request: HttpRequest object
    :return: {"message": "Hello world"}
    """
    return JsonResponse({"message": "Hello world"})


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
