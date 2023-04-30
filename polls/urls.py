from django.urls import path
from polls import views

urlpatterns = [
    path('test/', views.index, name='index')
]
