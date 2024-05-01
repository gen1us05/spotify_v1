from rest_framework import serializers
from .models import Artist, Album, Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name", "image", "last_update")

