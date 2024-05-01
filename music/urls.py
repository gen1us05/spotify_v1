from django.urls import path
from .views import LandingPageAPIView, ArtistAPIView

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artist/', ArtistAPIView.as_view(), name='artist'),
]
