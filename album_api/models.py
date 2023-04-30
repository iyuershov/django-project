# from enum import Enum
from django.db import models


# class AlbumCategory(Enum):
#     PRIVATE = 'private'
#     PUBLIC = 'public'


class Album(models.Model):
    id: int = models.IntegerField(primary_key=True)
    name: str = models.CharField(max_length=255)
    description: str = models.CharField(max_length=1000)
    category: str = models.CharField(max_length=255)


class Photo(models.Model):
    id: int = models.IntegerField(primary_key=True)
    name: str = models.CharField(max_length=255)
    description: str = models.CharField(max_length=1000)
    albums = models.ForeignKey(Album, on_delete=models.CASCADE)
