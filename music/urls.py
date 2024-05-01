from django.urls import path
from .views import LandingPageAPIView, ArtistAPIView, AlbumAPIView, SongsAPIView

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path('album/', AlbumAPIView.as_view(), name='album'),
    path('songs/', SongsAPIView.as_view(), name='songs'),
]
