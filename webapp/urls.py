from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('video/<str:filename>', views.stream_video, name='stream_video'),
]

