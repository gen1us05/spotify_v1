from django.urls import path, include
from .views import LandingPageAPIView, ArtistAPIView, SongSetAPIView, AlbumAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register("albums", viewset=AlbumAPIViewSet)
router.register("songs", viewset=SongSetAPIView)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path("", include(router.urls)),
    path("auth/", views.obtain_auth_token),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
