from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Album, Songs
from .serializers import ArtistSerializer

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

