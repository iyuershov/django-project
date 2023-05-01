from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from album_api.models import Album, Photo


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'description', 'category',)


class PhotoSerializer(ModelSerializer):
    albums = PrimaryKeyRelatedField(many=True, queryset=Album.objects.all(), required=False)

    class Meta:
        model = Photo
        fields = ('id', 'name', 'description', 'albums',)
