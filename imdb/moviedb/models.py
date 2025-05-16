from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    movies = models.ManyToManyField('Movie', through='Role', related_name='actors')

class Movie(models.Model):
    movie_name = models.CharField(max_length=255, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)

class Role(models.Model):
    role = models.CharField(max_length=255, null=True, blank=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')