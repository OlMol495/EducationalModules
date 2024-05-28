# Generated by Django 5.0.6 on 2024-05-27 15:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EdModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "module_number",
                    models.IntegerField(unique=True, verbose_name="номер модуля"),
                ),
                (
                    "title",
                    models.CharField(max_length=250, verbose_name="название модуля"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="описание модуля"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="course_images/",
                        verbose_name="превью модуля",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "модуль",
                "verbose_name_plural": "модули",
            },
        ),
        migrations.CreateModel(
            name="EdVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=250, verbose_name="название обучающего видео"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="описание обущающего видео"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="course_images/",
                        verbose_name="превью обучающего видео",
                    ),
                ),
                (
                    "video_link",
                    models.URLField(
                        blank=True, null=True, verbose_name="ссылка на видео"
                    ),
                ),
                (
                    "edmodule",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="education.edmodule",
                        verbose_name="название модуля",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "видео",
                "verbose_name_plural": "видео",
            },
        ),
    ]
