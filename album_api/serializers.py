from rest_framework.serializers import ModelSerializer
from album_api.models import Album, Photo


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
