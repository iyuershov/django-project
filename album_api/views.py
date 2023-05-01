from django.http import HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response

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

    # def create(self, request: Request, *args, **kwargs) -> Response:
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save(album=self.request.data.get("album"))
    #
    # def get_success_headers(self, data):
    #     try:
    #         return {"Location": str(data[self.lookup_field])}
    #     except (TypeError, KeyError):
    #         return {}
