from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from education.models import EdVideo
from education.permissions import IsModerator, IsOwner, IsAdmin
from education.serializers.edvideo import (EdVideoSerializer,
                                           EdVideoListSerializer, EdVideoDetailSerializer)


class EdVideoCreateAPIView(generics.CreateAPIView):
    """ Вьюшка на создание обучающего видео """
    serializer_class = EdVideoSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsAdmin]  # создавать могут только модеры и админ

    def perform_create(self, serializer):
        """ Привязывает юзера к размещаемому им видео """
        new_edvideo = serializer.save()
        new_edvideo.owner = self.request.user
        new_edvideo.save()


class EdVideoListAPIView(generics.ListCreateAPIView):
    """ Вьюшка на просмотр списка видео """
    serializer_class = EdVideoListSerializer
    queryset = EdVideo.objects.all()
    permission_classes = [IsAuthenticated]  # доступ имеют авторизованные юзеры


class EdVideoRetrieveAPIView(generics.RetrieveAPIView):
    """ Вьюшка на просмотр конкретного видео """
    serializer_class = EdVideoDetailSerializer
    queryset = EdVideo.objects.all()
    permission_classes = [IsAuthenticated]  # доступ имеют авторизованные юзеры


class EdVideoUpdateAPIView(generics.UpdateAPIView):
    """ Вьюшка на редактирование видео """
    serializer_class = EdVideoSerializer
    queryset = EdVideo.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
    # доступ имеет только хозяин и админ


class EdVideoDestroyAPIView(generics.DestroyAPIView):
    """ Dьюшка на удаление видео """
    serializer_class = EdVideoSerializer
    queryset = EdVideo.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
    # доступ имеет только хозяин и админ
