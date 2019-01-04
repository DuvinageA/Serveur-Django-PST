from django.db import models

# Create your models here.


class ImageRect(models.Model):
    top = models.FloatField()
    left = models.FloatField()
    bottom = models.FloatField()
    right = models.FloatField()
    description = models.TextField()


class TreatedImage(models.Model):
    link = models.URLField()
    path = models.TextField()
    rects = models.ManyToManyField(ImageRect)
