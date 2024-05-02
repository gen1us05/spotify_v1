from django.urls import path, include
from .views import LandingPageAPIView, ArtistAPIView, SongsAPIView, SongDetailAPIView, AlbumAPIViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("albums", viewset=AlbumAPIViewSet)


urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path("", include(router.urls)),
    path('songs/', SongsAPIView.as_view(), name='songs'),
    path('songs/<int:id>/', SongDetailAPIView.as_view(), name='songs-detail'),
]
