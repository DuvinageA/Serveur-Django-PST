from rest_framework import serializers
from djangorest.treated_image.models import TreatedImage, ImageRect


class ImageRectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ImageRect
        fields = '__all__'


class TreatedImageSerializer(serializers.HyperlinkedModelSerializer):

    rects = ImageRectSerializer(many=True)

    class Meta:
        model = TreatedImage
        fields = '__all__'

    def create(self, validated_data):
        rects_data = validated_data.pop('rects')
        image = TreatedImage.objects.create(**validated_data)
        image.save()
        for i in range(len(rects_data)):
            rect = ImageRect.objects.create(**rects_data[i])
            rect.save()
            image.rects.add(rect)
        return image

    def update(self, instance, validated_data):
        new_rects_data = validated_data.pop('rects')
        for rect in instance.rects.all():
            instance.rects.filter(id=rect.id).delete()
        for i in range(len(new_rects_data)):
            rect = ImageRect.objects.create(**new_rects_data[i])
            rect.save()
            instance.rects.add(rect)
        instance.save()
        return instance
