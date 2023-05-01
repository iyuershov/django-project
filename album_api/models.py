from django.db import models


class Album(models.Model):
    CATEGORIES = (
        (1, 'private'),
        (2, 'public')
    )
    id: int = models.IntegerField(primary_key=True)
    name: str = models.CharField(max_length=255)
    description: str = models.CharField(max_length=1000, null=True)
    category: int = models.IntegerField(choices=CATEGORIES, default=1)

    def __str__(self):
        return self.name


class Photo(models.Model):
    id: int = models.IntegerField(primary_key=True)
    name: str = models.CharField(max_length=255)
    description: str = models.CharField(max_length=1000, null=True)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.name
