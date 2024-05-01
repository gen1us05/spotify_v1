from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Album, Songs
from .serializers import ArtistSerializer, AlbumSerializer, SongsSerializer

class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"Get api": "hi dv"})

    def post(self, request):
        return Response(data={"Post api": "This is post request"})


class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        artist_serializer = ArtistSerializer(artists, many=True)
        return Response(data=artist_serializer.data)

class AlbumAPIView(APIView):
    def get(self, request):
        album = Album.objects.all()
        artist_serializer = AlbumSerializer(album, many=True)
        return Response(data=artist_serializer.data)


class SongsAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializers = SongsSerializer(songs, many=True)
        return Response(data=serializers.data)

