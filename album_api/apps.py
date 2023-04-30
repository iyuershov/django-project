from django.apps import AppConfig


class AlbumApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'album_api'
    verbose_name = 'Album API methods'
    description = 'API Methods for working with albums'
