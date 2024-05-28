from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class EdModule(models.Model):
    """ Образовательный модуль, который состоит из обучающих видео """
    module_number = models.IntegerField(unique=True, verbose_name='номер модуля')
    title = models.CharField(max_length=250, verbose_name='название модуля')
    description = models.TextField(**NULLABLE, verbose_name='описание модуля')
    image = models.ImageField(
        upload_to='course_images/', **NULLABLE, verbose_name='превью модуля'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE
    )

    def __str__(self):
        return f"образовательный модуль {self.title}"

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'


class EdVideo(models.Model):
    """ Модель урока """
    title = models.CharField(max_length=250, verbose_name='название обучающего видео')
    description = models.TextField(**NULLABLE, verbose_name='описание обущающего видео')
    image = models.ImageField(
        upload_to='course_images/', **NULLABLE, verbose_name='превью обучающего видео'
    )
    video_link = models.URLField(**NULLABLE, verbose_name='ссылка на видео')
    edmodule = models.ForeignKey(
        EdModule, **NULLABLE, on_delete=models.SET_NULL, verbose_name='название модуля'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE
    )

    def __str__(self):
        return f"обучающее видео {self.title}"

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'видео'
