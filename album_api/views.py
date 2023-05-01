from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from album_api.models import Album, Photo
from album_api.serializers import AlbumSerializer, PhotoSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def hello_world_view(request: Request) -> Response:
    """
    Метод для тестирования инициализации приложения
    :param request: Request object
    :return: {"message": "Hello world"}
    """
    return Response({"message": "Hello world"})


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
