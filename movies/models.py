from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.IntegerField()
    poster = models.ImageField()

    def __str__(self):
        return self.name
