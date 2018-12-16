from django.shortcuts import render
from djangorest.treated_image.models import TreatedImage, ImageRect
from djangorest.treated_image.serializers import TreatedImageSerializer, ImageRectSerializer
from rest_framework import viewsets

# Create your views here.


class TreatedImageViewSet(viewsets.ModelViewSet):
    queryset = TreatedImage.objects.all()
    serializer_class = TreatedImageSerializer


class ImageRectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImageRect.objects.all()
    serializer_class = ImageRectSerializer

