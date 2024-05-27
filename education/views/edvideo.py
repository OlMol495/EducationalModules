from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from education.models import EdVideo
from education.permissions import IsModerator, IsOwner
from education.serializers.edvideo import (EdVideoSerializer,
                                           EdVideoListSerializer, EdVideoDetailSerializer)


class EdVideoCreateAPIView(generics.CreateAPIView):
    """ Вьюшка на создание обучающего видео """
    serializer_class = EdVideoSerializer
    permission_classes = [IsAuthenticated, IsModerator]  # создавать могут только модеры

    def perform_create(self, serializer):
        """ Привязывает юзера к размещаемому им видео """
        new_edvideo = serializer.save()
        new_edvideo.owner = self.request.user
        new_edvideo.save()


class EdvideoListAPIView(generics.ListCreateAPIView):
    """вьюшка на просмотр списка уроков"""
    serializer_class = EdVideoListSerializer
    queryset = EdVideo.objects.all()
    permission_classes = [IsAuthenticated]  # доступ имеют авторизованные юзеры


class EdVideoRetrieveAPIView(generics.RetrieveAPIView):
    """ Вьюшка на просмотр конкретного видео """
    serializer_class = EdVideoDetailSerializer
    queryset = EdVideo.objects.all()
    permission_classes = [IsAuthenticated]  # доступ имеют авторизованные юзеры


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Вьюшка на редактирование видео """
    serializer_class = EdVideoSerializer
    queryset = EdVideo.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    # доступ имеет только хозяин


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Dьюшка на удаление видео """
    serializer_class = EdVideoSerializer
    queryset = EdVideo.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    # доступ имеет только хозяин
