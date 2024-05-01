from django.db import models



class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    last_updated = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    cover = models.ImageField()
    last_updated = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)


class Songs(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    last_updated = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

