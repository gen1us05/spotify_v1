from django.db.migrations import serializer
from django.db.transaction import atomic
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Album, Songs
from .serializers import ArtistSerializer, AlbumSerializer, SongsSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


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


class AlbumAPIViewSet(ModelViewSet):
    # def get_queryset(self):
    #     return Album.objects.all()

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )





class SongSetAPIView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'album__title', 'album__artist__name')
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['Post'])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        with atomic():
            song.listened += 1
            song.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.filter(status=True)
        songs = songs.order_by('-listened')[:3]
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['Post'])
    def albom(self, request, *args, **kwargs):
        song = self.get_object()
        album = song.album
        serializer = AlbumSerializer(album)
        return Response(data=serializer)

    @action(detail=True, methods=['Post'])
    def artist(self, request, *args, **kwargs):
        song = self.get_object()
        artist = song.album.artist
        serializer = ArtistSerializer(artist)
        return Response(data=serializer)



    # def get(self, request, id):
    #
    #     try:
    #         song = Songs.objects.get(id=id)
    #         serializers = SongsSerializer(song)
    #         return Response(data=serializers.data)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    # def patch(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     serializers = SongsSerializer(instance=song, data=request.data, partial=True)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(data=serializers.data, status=status.HTTP_200_OK)
    #
    #     return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def put(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     serializers = SongsSerializer(instance=song, data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(data=serializers.data, status=status.HTTP_200_OK)
    #
    #     return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # def delete(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     song.delete()
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)



