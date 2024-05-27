from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import EdModule, EdVideo
from education.validators import ValidateVideoLink


class EdVideoSerializer(serializers.ModelSerializer):
    """ Базовый сериализатор для урока """

    class Meta:
        model = EdVideo
        fields = '__all__'
        validators = [
            ValidateVideoLink(field='video_link')
        ]


class EdVideoListSerializer(serializers.ModelSerializer):
    """ Сериализатор для списка видео с указанием названия модуля,
    к которому они относятся """
    edmodule = SlugRelatedField(slug_field='title', queryset=EdModule.objects.all())

    class Meta:
        model = EdVideo
        fields = ('title', 'edmodule',)  # вывод ограничен названием видео и модуля


class EdVideoDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для деталей видео с указанием названия модуля, к которому оно относится """
    edmodule = SlugRelatedField(slug_field='title', queryset=EdModule.objects.all())

    class Meta:
        model = EdVideo
        fields = '__all__'
