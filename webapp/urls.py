from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .sitemaps import sitemaps

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('research/', views.research, name='research'),
    path('contact/', views.contact, name='contact'),
    path('video/<str:filename>', views.stream_video, name='stream_video'),
    path('robotics/kancha/', views.kancha, name='kancha'),
    path('share/kancha-media', views.share_media, name='share_media'),
    path('media/manage', views.media_manager, name='media_manager'),
    path('media/<str:slot>', views.serve_media, name='serve_media'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', views.robots, name='robots'),
]
