from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from education.models import EdModule
from education.permissions import IsModerator, IsOwner
from education.serializers.edmodule import EdModuleSerializer, EdModuleDetailSerializer


class EdModuleViewSet(viewsets.ModelViewSet):
    """  Вьюшка для модели образовательного модуля """
    queryset = EdModule.objects.all()
    permission_classes = [IsAuthenticated]
    default_serializer = EdModuleSerializer
    serializers = {
        'retrieve': EdModuleDetailSerializer
    }

    # def __init__(self, **kwargs):
    #     super(EdModuleViewSet, self).__init__()

    def get_serializer_class(self):
        """ Переопределение сериализатора на просмотр деталей модуля """
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        """ Определяет допуски по разным действиям CRUD """
        if self.action == 'create':
            self.permission_classes = [IsModerator]
            # создавать может только модер
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
            # просмотр списка доступен авторизованным юзерам
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]
            # просмотр деталей доступен авторизованным юзерам
        elif self.action == 'update':
            self.permission_classes = [IsOwner]
            # вносить изменения может только владелец
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
            # удалить может только владелец
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """ Привязывает юзера к создаваемому им модулю """
        new_edmodule = serializer.save()
        new_edmodule.owner = self.request.user
        new_edmodule.save()
