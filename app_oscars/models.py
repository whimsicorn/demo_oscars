from django.db import models

class Films(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    director = models.CharField(max_length=30, null=True, blank=True)
    year = models.SmallIntegerField(null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200,null=True, blank=True)
    poster = models.CharField(max_length=20, null=True, blank=True)
