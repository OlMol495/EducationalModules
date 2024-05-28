from django.contrib import admin
from education.models import EdModule, EdVideo


@admin.register(EdModule)
class AdminEdModule(admin.ModelAdmin):
    list_display = ('module_number', 'title', 'description', 'image',)


@admin.register(EdVideo)
class AdminEdVideo(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'video_link', 'edmodule',)
