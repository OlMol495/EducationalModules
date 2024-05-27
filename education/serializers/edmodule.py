from rest_framework import serializers

from education.models import EdModule, EdVideo
from materials.serializers.lesson import LessonSerializer


class EdModuleSerializer(serializers.ModelSerializer):
    """ Базовый сериализатор для образовательных модулей """

    class Meta:
        model = EdModule
        fields = '__all__'


class EdModuleDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для просмотра деталей курса """
    edvideo_count = serializers.SerializerMethodField()  # количество видео в модуле
    edvideo = EdVideoSerializer(source='edvideo_set', many=True)
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = EdModule
        fields = '__all__'

    def get_edvideo_count(self, edmodule):
        """ Вычисление количества видео в модуле """
        return EdVideo.objects.filter(edmodule=edmodule).count()