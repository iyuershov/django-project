from django.urls import path
from album_api import views

urlpatterns = [
    path('hello/', views.hello_world_view, name='hello_world')
]
