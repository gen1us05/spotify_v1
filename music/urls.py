from django.urls import path, include
from .views import LandingPageAPIView, ArtistAPIView, SongSetAPIView, AlbumAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("albums", viewset=AlbumAPIViewSet)
router.register("songs", viewset=SongSetAPIView)



urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path("", include(router.urls)),
    # path("auth/", views.obtain_auth_token),
]
