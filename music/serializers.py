from rest_framework import serializers
from .models import Artist, Album, Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name", "image", "last_updated")

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Album
        fields = ("title", "cover", "artist")


class SongsSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Songs
        fields = ("__all__")



